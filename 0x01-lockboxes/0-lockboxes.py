#!/usr/bin/python3

def canUnlockAll(boxes):
    """Determines if all the boxes can be opened."""
    n = len(boxes)
    opened_boxes = set()
    keys = [0]

    while keys:
        key = keys.pop()
        if key not in opened_boxes:
            opened_boxes.add(key)
            for k in boxes[key]:
                if k not in opened_boxes:
                    keys.append(k)

    return len(opened_boxes) == n
