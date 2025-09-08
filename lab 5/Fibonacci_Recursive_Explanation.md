## Recursive Fibonacci: Code and Explanation

This project includes a simple implementation of the Fibonacci sequence using recursion and a minimal CLI to run it.

### What is the Fibonacci sequence?
The sequence is defined as:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) for n ≥ 2

### How the code works
- **Function**: `fibonacci_recursive(n: int) -> int`
  - Validates that `n` is non-negative.
  - Returns base cases for `n == 0` and `n == 1`.
  - Recursively computes `F(n-1) + F(n-2)` for `n >= 2`.

- **CLI**: `python task_3(cursor).py <n>` prints the nth Fibonacci number.
  - Use `--test` to run built-in sanity checks.

### Complexity
- **Time**: Exponential, approximately O(phi^n) where phi ≈ 1.618.
- **Space**: O(n) due to call stack depth.
- For larger `n`, consider memoization (caching) or an iterative approach.

### Examples
```bash
python task_3(cursor).py 10   # -> 55
python task_3(cursor).py --test
```

### File(s)
- `task_3(cursor).py`: Recursive implementation and CLI.


