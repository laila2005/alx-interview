#!/usr/bin/python3
def canUnlockAll(boxes):
    """Check if all boxes can be opened starting from box 0"""
    n = len(boxes)
    opened = set([0])
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if 0 <= key < n and key not in opened:
            opened.add(key)
            keys.update(boxes[key])
    
    return len(opened) == n
