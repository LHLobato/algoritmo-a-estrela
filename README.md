This repo implements the A* algorithm with two heuristics in python:

- $h_1(n)$: a counter for how much pieces are out of order.
- $h_2(n)$: Manhattan distance.

This is a memory intensive approach, with a huge footprint, even though we mitigate this problem with a explored state structure to cache explored states and to allow for path reconstruction.


# Running the code
We have sampled some experiments and their results on `assets/`, but if you insist, you can run the code with any python package manager. I do prefer `uv` and will be using it for the example. So, run:

syncing the .venv
```bash
uv sync
```

running the code
```bash
uv run main.py 
uv run main.py -v

```
