# Stack (Python)

Simple Stack implementation using a Python `list`.

Files:
- `stack.py`: Stack class with `push`, `pop`, `peek`, and `is_empty`.
- `test_stack.py`: `unittest` test cases.

Run tests:

```powershell
python -m unittest test_stack.py
```

Example:

```python
from stack import Stack

s = Stack()
s.push(1)
print(s.peek())  # 1
print(s.pop())   # 1
```
