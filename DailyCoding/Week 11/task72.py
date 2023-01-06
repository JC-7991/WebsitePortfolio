'''In a directed graph, each node is assigned an uppercase letter. 
We define a path's value as the number of most frequently-occurring 
letter along that path. For example, if a path in the graph goes through 
"ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.
Given a graph with n nodes and m directed edges, return the largest value path 
of the graph. If the largest value is infinite, then return null.
The graph is represented with a string and an edge list. The i-th 
character represents the uppercase letter of the i-th node. Each tuple 
in the edge list (i, j) means there is a directed edge from the i-th node 
to the j-th node. Self-edges are possible, as well as multi-edges.
For example, the following input graph:
ABACA
[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]
Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).
The following input graph:
A
[(0, 0)]
Should return null, since we have an infinite loop.'''

from typing import Dict, List, Optional, Set, Tuple

class GraphPath:

    def __init__(self, nodes: Set[str] = set(), letters: Dict[str, int] = dict()) -> None:
        self.nodes = nodes
        self.letters = letters

    def __repr__(self) -> str:
        return "nodes = {}, letters = {}".format(self.nodes, self.letters)


def strHelper(graph_path: GraphPath, node: str, adj_map: Dict[str, Set[str]]) -> List[GraphPath]:

    if node in graph_path.nodes:
        return [graph_path]

    new_nodes = graph_path.nodes.copy()
    new_nodes.add(node)
    new_letter_counts = graph_path.letters.copy()

    if node[0] not in new_letter_counts:
        new_letter_counts[node[0]] = 0

    new_letter_counts[node[0]] += 1

    new_graph_path = GraphPath(new_nodes, new_letter_counts)

    if node not in adj_map:
        return [new_graph_path]

    paths = list()

    for child_node in adj_map[node]:
        new_paths = strHelper(new_graph_path, child_node, adj_map)
        paths.extend(new_paths)

    return paths

def maxString(graph_string: str, edge_list: List[Tuple[int, int]]) -> Optional[int]:

    letters = dict()
    nodes = list()

    for char in graph_string:

        if char not in letters:
            letters[char] = 0

        else:
            letters[char] += 1

        nodes.append("{}{}".format(char, letters[char]))

    adj_map = dict()

    for start, end in edge_list:

        if nodes[start] not in adj_map:
            adj_map[nodes[start]] = set()

        if nodes[start] != nodes[end]:
            adj_map[nodes[start]].add(nodes[end])

    paths = list()
    graph_path = GraphPath()

    for node in adj_map:
        new_paths = strHelper(graph_path, node, adj_map)
        paths.extend(new_paths)

    maxValue = 0

    for path in paths:

        maxPath = max(path.letters.values())

        if maxPath > maxValue:
            maxValue = maxPath

    return maxValue if maxValue > 0 else None


if __name__ == "__main__":

    print(maxString("ABACA", [(0, 1), (0, 2), (2, 3), (3, 4)]))
    print(maxString("A", [(0, 0)]))