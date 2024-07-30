#!/usr/bin/python3
"""A function that can determine if all boxes can be opened"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened."""

    for key in range(1, len(boxes)):
        flag = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                flag = True
                break
        if not flag:
            return False

    return True
