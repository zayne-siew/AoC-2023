import sys
from random import shuffle
from copy import copy, deepcopy

def parse(file):
    graph = dict()
    with open(file, "r") as f:
        for l in f.read().strip().splitlines():
            node, neighbors = l.split(": ")
            neighbors = neighbors.split()
            if node not in graph:
                graph[node] = set(neighbors)
            else:
                graph[node] |= set(neighbors)
            for nnode in neighbors:
                if nnode not in graph:
                    graph[nnode] = set()
                graph[nnode].add(node)

    return graph


# Return the product of the cardinality of the two remaining nodes of
# the graph after contracting to `target` edges or fewer.
def karger(graph, target):
    edges = []

    graph = deepcopy(graph)

    # First we create a new representation: a list of edges
    for node in graph:
        neighbors = graph[node]
        for neighbor in copy(neighbors):
            edge = [node, neighbor]
            edges.append(edge)
            graph[node].discard(neighbor)
            graph[neighbor].discard(node)

    # We nuke the edges each time, so we save them.
    saved = edges

    # Now we keep running Karger until we get what we want
    while True:
        edges = deepcopy(saved)
        nodes = dict()
        nodesize = dict()

        for edge in edges:
            a, b = edge
            if a not in nodes:
                nodes[a] = []
            if b not in nodes:
                nodes[b] = []
            nodes[a].append(edge)
            nodes[b].append(edge)

        for node in nodes:
            nodesize[node] = 1

        # By shuffling, we can simply pop edges off the end
        shuffle(edges)

        while len(nodes) > 2:
            edge = edges.pop()
            a, b = edge

            # Skip self edges
            if a == b:
                continue

            # move all edges from b to a
            for edge in nodes[b]:
                # Rename the edge
                for i in range(2):
                    if edge[i] == b:
                        edge[i] = a

                nodes[a].append(edge)
            del nodes[b]

            # update the nodesize
            nodesize[a] += nodesize[b]
            del nodesize[b]

            # remove any self edges in a.
            newedges = []
            for edge in nodes[a]:
                x, y = edge
                if x != y:
                    newedges.append(edge)
            nodes[a] = newedges

        # We should now have exactly two nodes.
        # They should have identical sets of edges.
        keys = list(nodes)

        if len(nodes[keys[0]]) <= target:
            #print(f"nodes = {nodes}")
            #print(f"nodesizes = {nodesize}")
            break

    return nodesize[keys[0]] * nodesize[keys[1]]


def part1(data):
    return karger(data, 3)


data = parse('d25p1.txt')
print(f"part 1 = {part1(data)}")