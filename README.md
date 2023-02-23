# 8 puzzle solver

- [8 puzzle solver](#8-puzzle-solver)
  - [File directory](#file-directory)
  - [Puzzle format](#puzzle-format)
  - [How to run](#how-to-run)
  - [Run Part 2](#run-part-2)
  - [Run Part 3](#run-part-3)

## File directory

```txt
📁 8-puzzle
┣━━ main.py - parse command line arguments and run the program
┣━━ search.py - implements search algorithms and classes
┣━━ utils.py - implements utility functions like reading input file, printing output, heuristics, etc.
┣━━ perf_analysis_p2 - performance analysis for p2
┗━━ perf_analysis_p3 - performance analysis for p3
```

The following algorithms are implemented in search

1. BFS (Breath First Search)
2. IDS (Iterative deepening DFS)
3. A\* with misplaced title heuristic. (h1)
4. A\* with Manhattan distance heuristic (h2).
5. A\* with one more heuristic (invent or check the literature for this) (h3)

## Puzzle format

Sample input file : `easy.txt`

```txt
1 2 3
4 6 8
7 5 _
```

where `_` is the empty tile.

Goal state is

```txt
1 2 3
4 5 6
7 8 _
```

In code, puzzle is defined with tuples

```python
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
```

where `0` is the empty tile.

## How to run

Input: Two command line arguments:

1. File path and
2. Algorithm to be used `(BFS/IDS/h1/h2/h3)`

Output:

1. Total nodes generated (for A\* this includes nodes in closed list and fringe).
2. Total time taken.
3. Path length
4. A valid sequence of actions which will take the given state to the goal state.

```bash
python main.py --fPath <PATH_TO_FILE> --alg <ALGORITHM_NAME>
```

example run

```bash
python main.py --fPath Test_p2/easy.txt --alg h1
## expected output
# Total nodes generated: 12
# Total time taken:, 0 sec 64 microSec
# Path length: 4
# A valid sequence of actions: DRUL
```

## Run Part 2

This runs 5 states given in Part2 for all the 5 algorithms (i.e., in total
there’ll be 25 runs).

Run on sample

```bash
python perf_analysis_p2.py --in_dir Test_p2 --out_dir test_out
```

expected output

```txt
--Fpath easy.txt --alg BFS
Total nodes generated: 29
Total time taken:, 0 sec 73 microSec
Path length: 4
A valid sequence of actions: DRUL

--Fpath easy.txt --alg IDS
Total nodes generated: 48
Total time taken:, 0 sec 102 microSec
Path length: 4
A valid sequence of actions: DRUL

--Fpath easy.txt --alg h1
Total nodes generated: 12
Total time taken:, 0 sec 63 microSec
Path length: 4
A valid sequence of actions: DRUL

--Fpath easy.txt --alg h2
Total nodes generated: 12
Total time taken:, 0 sec 93 microSec
Path length: 4
A valid sequence of actions: DRUL

--Fpath easy.txt --alg h3
Total nodes generated: 12
Total time taken:, 0 sec 116 microSec
Path length: 4
A valid sequence of actions: DRUL

--Fpath easy.txt --alg BFS
Total nodes generated: 29
Total time taken:, 0 sec 75 microSec
Path length: 4
A valid sequence of actions: DRUL

--Fpath easy.txt --alg IDS
Total nodes generated: 48
Total time taken:, 0 sec 99 microSec
Path length: 4
A valid sequence of actions: DRUL

--Fpath easy.txt --alg h1
Total nodes generated: 12
Total time taken:, 0 sec 68 microSec
Path length: 4
A valid sequence of actions: DRUL

--Fpath easy.txt --alg h2
Total nodes generated: 12
Total time taken:, 0 sec 101 microSec
Path length: 4
A valid sequence of actions: DRUL

--Fpath easy.txt --alg h3
Total nodes generated: 12
Total time taken:, 0 sec 112 microSec
Path length: 4
A valid sequence of actions: DRUL

```

Run on part 2

```bash
python perf_analysis_p2.py --in_dir Part2 --out_dir submit
```

## Run Part 3

In this part, we compare the performance of the algorithms

1. In file part3 you’ll find 60 8-puzzles. 20 from each of 8, 15, and 24 levels, where level indicates the optimal path length of the state from the goal.
2. For states in each level solve the puzzle and calculate the average run time and average nodes generated for all the five algorithms.

Run on sample

```bash
python perf_analysis_p3.py --in_dir Test_p3 --out_dir test_out
```

expected output

```txt
Level: L3
{'BFS': (29.0, '00:00:000081'),
 'IDS': (48.0, '00:00:000100'),
 'h1': (12.0, '00:00:000073'),
 'h2': (12.0, '00:00:000103'),
 'h3': (12.0, '00:00:000119')}
Level: L2
{'BFS': (29.0, '00:00:000086'),
 'IDS': (48.0, '00:00:000101'),
 'h1': (12.0, '00:00:000073'),
 'h2': (12.0, '00:00:000108'),
 'h3': (12.0, '00:00:000122')}
Level: L1
{'BFS': (29.0, '00:00:000082'),
 'IDS': (48.0, '00:00:000102'),
 'h1': (12.0, '00:00:000075'),
 'h2': (12.0, '00:00:000144'),
 'h3': (12.0, '00:00:000128')}
```

where the first number in tuple is the average nodes generated and the second number is the average time taken.

Run on part 3

```bash
python perf_analysis_p3.py --in_dir Part3 --out_dir submit
```
