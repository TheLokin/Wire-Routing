<h1 align="center">Wire Routing</h1>

## Introduction
This project use *telingo* to solve a variant of the wire routing problem as a multi-robot planning problem. Given a rectangular
grid, the problem consists in joining pairs of points (named with the same letter {a,b,c,...}) with a continuous line that does
not intersect with lines for other pairs. Some of the grid cells are marked as obstacles.

## Implementation
The input will be given as a text file where the two first lines respectively contain the number of rows and columns of the
grid. We use "." to represent an (initially) empty cell, "#" to represent an obstacle and letters {a,b,c,...} to mark pairs of
points to be joined. The output is a text file where each "wire" is traced using the corresponding letter. As an example:

Initial configuration: two wires, a and b, are needed.
```
6
7
.a....b
.......
..b..##
.##..##
.##...a
.....##
```

A possible solution.
```
.a..bbb
aa..b..
a.bbb##
a##..##
a##.aaa
aaaaa##
```

## Execution

The examples folder contains a set of benchmarks of different sizes. Solutions are not included because several minimal
solutions can be obtained.
```
./wire.py [-h] [-o] input

-h            show this help message and exit
-o            calculate optimum path
-input        path of the wire routing instance
```
