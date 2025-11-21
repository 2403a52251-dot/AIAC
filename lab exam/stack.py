"""stack.py

Simple Stack data structure implemented using a Python list.

Provides push, pop, peek, and is_empty methods.
"""
# One-shot prompt used to request the `is_empty` method implementation is
# saved separately in `ONE_SHOT_PROMPT.txt` in this project root. The method
# `is_empty()` returns True when the stack contains no items and False
# otherwise. This file's code implements that requirement.
#
# (See `ONE_SHOT_PROMPT.txt` for the exact one-shot instruction content.)
from typing import Generic, List, TypeVar

T = TypeVar('T')


class Stack(Generic[T]):
    """A simple LIFO stack backed by a Python list.

    Examples:
        >>> s = Stack[int]()
        >>> s.push(1)
        >>> s.peek()
        1
    """

    def __init__(self) -> None:
        """Initialize an empty stack."""
        # Internal list holding stack items; end of list is the top of the stack.
        self._items: List[T] = []

    def push(self, item: T) -> None:
        """Push `item` onto the top of the stack.

        Args:
            item: The item to push.
        """
        self._items.append(item)

    def pop(self) -> T:
        """Remove and return the top item from the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        """Return the top item without removing it.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """Return True if the stack has no items, False otherwise.

        This is the additional method requested by the one-shot instruction.
        """
        return len(self._items) == 0

    def __len__(self) -> int:
        """Return the number of items in the stack."""
        return len(self._items)
