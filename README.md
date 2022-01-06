# ShortestPath

This is a my version of Shortest Path Algorithm inspired in [Edsger Dijkstra - Shortest Path Alogorithm (1959)](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) using Python3.

> The algorithm exists in many variants. Dijkstra's original algorithm found the shortest path between two given nodes,[6] but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree. 

![Dijkstra Graph](https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif "Dijkstra Graph")

Todo:
- [x] Shortest path on 1 level.
- [x] Shortest path on 2 levels.
- [ ] Shortest path on 3 levels.
- [ ] Shortest path on infinity levels.
- [ ] Better Refactor.
- [ ] Optimization.


## Implementation example in main.py
```python
python3 main.py
```

## Goal:

Implements a Shortest Path Algorithm with infinity levels as shown in the image below. <br />
![Dijkstra Algorithm InfinityNodes](https://upload.wikimedia.org/wikipedia/commons/2/23/Dijkstras_progress_animation.gif "Dijkstra Algorithm InfinityNodes")
> Illustration of Dijkstra's algorithm finding a path from a start node (lower left, red) to a goal node (upper right, green) in a robot motion planning problem. Open nodes represent the "tentative" set (aka set of "unvisited" nodes). Filled nodes are visited ones, with color representing the distance: the greener, the closer. Nodes in all the different directions are explored uniformly, appearing more-or-less as a circular wavefront as Dijkstra's algorithm uses a heuristic identically equal to 0. [link](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
