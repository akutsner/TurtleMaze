#  TurtleMaze

A random **maze generator and solver** built with Python's `turtle` graphics, using a modified **depth-first search**.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

<!-- TIP: add a screenshot of a generated maze here -->
<!-- ![maze](maze.png) -->

## How it works

The canvas is split into a grid of cells. Starting from one cell, the algorithm:

1. Looks at the unvisited neighbours to the north, east, south and west
2. Picks one at random, knocks down the wall between them and moves there
3. Backtracks when it hits a dead end, and keeps going until every cell has been visited

This gives a *perfect maze*: every cell can be reached, and there's exactly one path between any two points.

### Modes

- **Solve mode:** draws the path from start to finish once the maze is built
- **Strange mode** (set `strange = True` in `Maze.py`): changes how the next neighbour is chosen, which gives more unpredictable, winding corridors

## Running it

```bash
git clone https://github.com/akutsner/TurtleMaze.git
cd TurtleMaze
python Maze.py
```

You'll be asked for:

```
Height 100 - 500: 400
Length 100 - 500: 400
Scale 10 - 30: 20
Solve? (y/n): y
```

No dependencies: `turtle` ships with Python.
