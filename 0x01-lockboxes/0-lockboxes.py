#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    """Determine if all the boxes can be opened."""
    n = len(boxes)
    open_boxes = set([0])
    closed_boxes = set(boxes[0]).difference(set([0]))
    while len(closed_boxes) > 0:
        box_item = closed_boxes.pop()
        if not box_item or box_item >= n or box_item < 0:
            continue
        if box_item not in open_boxes:
            closed_boxes = closed_boxes.union(boxes[box_item])
            open_boxes.add(box_item)
    return n == len(open_boxes)
