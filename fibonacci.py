# fibonacci.py
"""Simple Fibonacci series implementation.

Provides a function `fib_series(n)` that returns a list containing the first `n`
Fibonacci numbers (starting from 0). When run as a script, it prints the series
for a user‑provided `n` (default 10).
"""

def fib_series(n: int) -> list[int]:
    """Return a list of the first `n` Fibonacci numbers.

    Args:
        n: Number of terms to generate. Must be non‑negative.
    Returns:
        List of integers representing the Fibonacci sequence.
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series


if __name__ == "__main__":
    import sys
    # Allow optional command‑line argument for number of terms
    try:
        count = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    except ValueError:
        print("Please provide a valid integer for the number of terms.")
        sys.exit(1)
    print(f"First {count} Fibonacci numbers: {fib_series(count)}")
