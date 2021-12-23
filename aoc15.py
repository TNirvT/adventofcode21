import numpy as np
import sys

INFINITE = sys.maxsize

class Graph:
    def __init__(self, nodes: list, init_graph: dict) -> None:
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        graph = {x: None for x in nodes}
        graph.update(init_graph)
        return graph

    def get_nodes(self):
        return self.nodes

    def get_neighbors(self, node: tuple[int, int]) -> list[tuple[int, int]]:
        neightbors = []
        adjacents = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for adjacent in adjacents:
            adj_node = tuple(np.add(node, adjacent))
            if adj_node in self.nodes:
                neightbors.append(adj_node)
        return neightbors

    def value(self, goto_node) -> int:
        return self.graph[goto_node]

def open_file(file_name):
    with open(file_name, "r") as f:
        inputs = []
        for line in f:
            inputs.append([int(x) for x in line.rstrip()])
    return inputs

def read_map(inputs: list[list[int]]):
    # important: the 1st entry is start pt, and the last one is end pt
    nodes = list(np.ndindex((len(inputs), len(inputs[0]))))
    init_graph = {x: int(inputs[x[0]][x[1]]) for x in nodes}
    return nodes, init_graph

def dijkstra(graph: Graph):
    end = graph.nodes[-1]
    unvisited = set(graph.get_nodes()) # changed from list, becoz slow
    path = {x: INFINITE for x in unvisited}
    path[(0, 0)] = 0
    prev_nodes = {}
    while True:
        current_min_node = min(unvisited, key=path.get)

        neighbors = graph.get_neighbors(current_min_node)
        for neighbor in neighbors:
            if neighbor not in unvisited:
                continue

            tentative_value = path[current_min_node] + graph.value(neighbor)
            if tentative_value < path[neighbor]:
                path[neighbor] = tentative_value
                prev_nodes[neighbor] = current_min_node

        unvisited.remove(current_min_node)
        if current_min_node == end:
            return prev_nodes, path

def dijkstra2(graph: dict[tuple[int, int], int]):
    end = list(graph.keys())[-1]
    unvisited = set(graph.keys())

    current_min_node = (0, 0)
    path = {(0, 0): 0}
    while True:
        neighbors = [
            (current_min_node[0]-1, current_min_node[1]),
            (current_min_node[0]+1, current_min_node[1]),
            (current_min_node[0], current_min_node[1]-1),
            (current_min_node[0], current_min_node[1]+1)
        ]
        for neighbor in neighbors:
            if neighbor not in unvisited:
                continue

            tentative_value = path[current_min_node] + graph[neighbor]
            value = path.get(neighbor)
            if value == None or tentative_value < value:
                path[neighbor] = tentative_value

        unvisited.remove(current_min_node)
        del path[current_min_node]
        current_min_node = min(path, key=path.get)
        if current_min_node == end:
            return path

def map_x5x5(inputs: list[list[int]]):
    def map_shift(inputs):
        shift_map = []
        for line in inputs:
            shift_line = [x+1 if x+1 <= 9 else 1 for x in line]
            shift_map.append(shift_line)
        return shift_map

    new_map = list(inputs)
    shift_right = list(inputs)
    for _ in range(5 -1):
        shift_right = map_shift(shift_right)
        new_map = np.concatenate((new_map, shift_right), axis=1)

    shift_down = list(new_map)
    for _ in range(5 -1):
        shift_right = map_shift(shift_right)
        shift_down = [x[len(inputs[0]):] for x in shift_down]
        shift_down = np.concatenate((shift_down, shift_right), axis=1)
        new_map = np.concatenate((new_map, shift_down), axis=0)
    return new_map

if __name__ == "__main__":
    # inputs = open_file("test.txt")
    inputs = open_file("aoc15.txt")

    nodes, init_graph = read_map(inputs)
    graph = Graph(nodes, init_graph)
    prev_nodes, path = dijkstra(graph)
    print(f"Part one: {path[graph.nodes[-1]]}")

    new_map = map_x5x5(inputs)
    nodes, init_graph = read_map(new_map)
    path = dijkstra2(init_graph)
    print(f"Part two: {path[list(init_graph.keys())[-1]]}")
