### Prime Factor Calculator with File Caching

This is a Python console application designed to calculate the unique prime factors of a positive integer. It implements a file-based caching mechanism to store and retrieve previously calculated results, significantly improving performance on repeated inputs.

The application is structured to demonstrate robust error handling, efficient algorithms, and best practices in input validation and data persistence.

### 🌟 Features

Efficient Prime Factorization: Uses an optimized trial division algorithm to quickly find unique prime factors.

Persistent File Caching: Stores results in prime_factors_cache.json for rapid retrieval.

Cache Hit: Retrieves results instantly and measures the negligible lookup time.

Cache Miss: Calculates factors, measures the computation time, and saves the result to the cache.

Graceful Exit: The user can exit the program at any time by typing 'q' or 'quit'.

Output Logging: Appends the results of every run (factors found and duration) to prime_factors_output.txt.

Input Validation: Ensures the user enters a natural number greater than 1, asking them to retry if the input is invalid or less than or equal to 1.

### 📁 File Structure

The project primarily consists of one Python file and two data files it interacts with:


prime_number.py: The main script containing the factoring algorithm, caching logic, and user interface.

prime_factors_cache.json: The file used for persistence (database). Stores the factors and the original calculation time for fast lookups.

prime_factors_output.txt: The log file where every result (number, factors, time taken) is appended for history tracking.

Primenumbers.pdf: Assignment instructions

### 💻 How to Run the Program

Prerequisites

You only need Python 3 installed on your system.

Running the Script

Navigate to the directory where prime_number.py is located using your terminal (e.g., PowerShell or Command Prompt).

Execute the script:

python prime_number.py

### Example output
PS C:\Users\seyda\prime_number> python prime_number.py
--- Prime Factor Calculator  ---
Enter a positive number to factor (must be > 1, or 'q' to quit): 26541
INFO: Cache file 'prime_factors_cache.json' not found. Creating a new one.
Calculating prime factors for 26541...
INFO: Result saved to database for future fast access.

--- Results ---
Prime factor found: 3
Prime factor found: 983
It took 0.0000 seconds to calculate.
INFO: Result saved to output file: 'prime_factors_output.txt'
