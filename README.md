This repo implements the A* algorithm with two heuristics in python:

- $h_1(n)$: a counter for how much pieces are out of order.
- $h_2(n)$: Manhattan distance.

This is a memory intensive approach, with a huge footprint, even though we mitigate this problem with a explored state structure to cache explored states and to allow for path reconstruction.
