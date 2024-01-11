#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """
    Check if all boxes in the list can be unlocked.

    Args:
        boxes (list): A list of lists representing the lockboxes
        and their keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    unlocked = set([0])
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == len(boxes)
