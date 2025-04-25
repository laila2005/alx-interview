#!/usr/bin/python3
"""Module for checking if all lockboxes can be opened."""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Args:
        boxes (list of lists): A list where each index represents a box,
        and each element is a list of keys in that box.
    
    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    opened = set([0])
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if 0 <= key < n and key not in opened:
            opened.add(key)
            keys.update(boxes[key])

    return len(opened) == n
