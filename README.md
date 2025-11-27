# Prime Factor Calculator with File Caching

A simple but efficient Python console application for calculating the **unique prime factors** of a positive integer.  

The program uses a **file-based cache** to store previously computed results, so repeated inputs are returned almost instantly. It also logs every run to a text file for later inspection.

---

##  Features

- **Efficient prime factorization**  
  Uses an optimized trial division algorithm to find **unique** prime factors of a given number.

- **Persistent file caching**  
  Results are stored in `prime_factors_cache.json` to speed up subsequent runs with the same input.

- **Cache hit / miss reporting**  
  - **Cache hit**: Factors are loaded from the cache and lookup time is measured (typically negligible).  
  - **Cache miss**: Factors are computed, time is measured, and the result is added to the cache.

- **Graceful exit**  
  The program can be exited at any time by entering `q` or `quit`.

- **Output logging**  
  Every run is appended to `prime_factors_output.txt`, including:
  - the input number  
  - the prime factors  
  - the time taken to compute or retrieve them  
  - whether it was a cache hit or miss (if implemented)

- **Robust input validation**  
  Ensures that the user enters a **natural number greater than 1**.  
  If the input is invalid (non-numeric, negative, 0, or 1), the user is asked to try again.

---

##  Project Structure


.
├── prime_number.py               # Main script (logic, caching, and console UI)
├── prime_factors_cache.json      # Cache file: number -> (factors, computation time)
├── prime_factors_output.txt      # Log file: history of all runs
└── Primenumbers.pdf              # Assignment / specification document

##  Running the program 

- Prerequisites: Python 3 installed

In the directory containing prime_number.py, run:
- python prime_number.py

## AI Acknowledgment
I used AI tools to accelerate development and improve code quality, while keeping full control over all architectural and implementation decisions.

- Architecture (Gemini): Helped outline the initial structure and modular approach.

. Quality Review (ChatGPT & GROK): Provided critical feedback on efficiency, error handling, and Pythonic improvements.

This multi-step approach improved iteration speed, but all final design choices and code decisions were made by me.