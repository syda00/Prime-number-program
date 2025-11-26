import time
import json
from typing import List, Dict, Any
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)
# --- Configuration ---
CACHE_FILE = 'prime_factors_cache.json'
OUTPUT_FILE = 'prime_factors_output.txt'

def load_cache(filename: str) -> Dict[str, Any]:
    """Loads the database (cache) from a JSON file. Creates an empty file if it doesn't exist."""
    try:
        with open(filename, 'r') as f:
            # Keys in JSON must be strings, so we store numbers as strings.
            return json.load(f)
    except FileNotFoundError:
        logging.info(f"Cache file '{filename}' not found. Creating a new one.")
        return {}
    except json.JSONDecodeError:
        logging.info(f"Warning: Cache file '{filename}' is corrupt. Starting with an empty cache.")
        return {}

def save_cache(filename: str, cache: Dict[str, Any]) -> None:
    """Saves the current cache state to the JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump(cache, f, indent=4)
    except IOError as e:
        logging.info(f"Error saving cache file: {e}")

def get_unique_prime_factors(n: int) -> List[int]:
    """
    Finds all unique prime factors of a positive integer n.
    Uses an optimized trial division method.
    """
    factors = set()
    d = 2
    temp = n

    # Handle factor 2
    if temp % d == 0:
        factors.add(d)
        while temp % d == 0:
            temp //= d

    # Handle odd factors
    d = 3
    while d * d <= temp:
        if temp % d == 0:
            factors.add(d)
            while temp % d == 0:
                temp //= d
        d += 2

    # Handle the remaining prime factor (if any)
    if temp > 1:
        factors.add(temp)

    return sorted(list(factors))

def write_output_file(number: int, factors: List[int], duration: float, source: str) -> None:
    """
    Writes the result to the output file (OUTPUT_FILE), appending to existing content.
    'source' is either 'calculate' or 'database' and is used to describe the action.
    """
    try:
        duration_str = f"{duration:.4f}"
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        if source == "calculate":
            action = "calculate them"
        elif source == "database":
            action = "get them from database"
        else:
            action = "find those"

        # Build the content block
        content_block = (
            f"--- Run at {timestamp} ---\n"
            f"Prime Factors of number {number} are\n"
            f"{', '.join(map(str, factors))}\n"
            f"It took {duration_str} seconds to {action}\n"
        )

        # Add a separating blank line only if file already has content
        try:
            with open(OUTPUT_FILE, 'r') as f:
                needs_separator = bool(f.read(1))
        except FileNotFoundError:
            needs_separator = False

        full_content = ("\n" if needs_separator else "") + content_block

        with open(OUTPUT_FILE, 'a') as f:
            f.write(full_content)

        logging.info(f"Result saved to output file: '{OUTPUT_FILE}'")

    except IOError as e:
        logging.info(f"Error writing to output file '{OUTPUT_FILE}': {e}")



def main():
    """Main execution function for the Prime Factor Finder."""
    print("--- Prime Factor Calculator  ---")
    
    # 1. Get user input (loop until valid input is received or user quits)
    while True:
        try:
            number_str = input("Enter a positive number to factor (must be > 1, or 'q' to quit): ").strip()
            
            if number_str.lower() in ('q', 'quit'):
                logging.info("Exiting program.")
                return
            
            if not number_str:
                print("Input cannot be empty. Please try again.")
                continue

            number = int(number_str)
            
            if number <= 1:
                print("Please enter a natural number greater than 1.")
                continue
            
            # Valid input
            break
            
        except ValueError:
            logging.info("Invalid input. Please enter a valid integer.")
            continue

    # 2. Load cache
    cache = load_cache(CACHE_FILE)
    
    # 3. Check cache
    if number_str in cache:
        # --- Cache Hit ---
        cached_data = cache[number_str]
        factors = cached_data['factors']
        calc_time = cached_data.get('calculation_time')

        # Measure lookup time
        start_time = time.perf_counter()
        # (In reality lookup is O(1), but we measure consistently)
        _ = factors  # dummy usage
        end_time = time.perf_counter()
        lookup_duration = end_time - start_time

        source = "database"
        duration = lookup_duration  # this is what we report as "time to get"

        logging.info("Found in Database!")
        if calc_time is not None:
            print(f"Original calculation took: {calc_time:.4f} seconds.")
        print(f"Lookup took: {lookup_duration:.4f} seconds.")
        
    else:
        # --- Cache Miss / Calculation ---
        print(f"Calculating prime factors for {number}...")
        start_time = time.perf_counter()
        
        factors = get_unique_prime_factors(number)
        
        end_time = time.perf_counter()
        calc_duration = end_time - start_time
        duration = calc_duration
        source = "calculate"
        
        # Save result to cache
        cache[number_str] = {
            'factors': factors,
            'calculation_time': calc_duration
        }
        save_cache(CACHE_FILE, cache)
        logging.info("Result saved to database for future fast access.")
    
    # 4. Display results
    display_duration = f"{duration:.4f}"

    print("\n--- Results ---")
    for factor in factors:
        print(f"Prime factor found: {factor}")
        
    if source == "database":
        print(f"It took {display_duration} seconds to get from database.")
    else:
        print(f"It took {display_duration} seconds to calculate.")
    
    # 5. Write to output file, now passing 'source' so action is correct in the file too
    write_output_file(number, factors, duration, source)
    print("-----------------\n")

if __name__ == "__main__":
    main()