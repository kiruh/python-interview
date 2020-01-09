from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def breadth_first_search(self, start):
        visited = {}
        visited[start] = True

        queue = []
        queue.append(start)

        while queue:
            current = queue.pop(0)
            neighbours = self.graph[current]
            for neighbour in neighbours:
                if visited.get(neighbour):
                    continue
                queue.append(neighbour)
                visited[neighbour] = True

    def depth_first_search(self, start):
        visited = {}
        visited[start] = True

        stack = []
        stack.append(start)

        while stack:
            current = stack.pop()
            neighbours = self.graph[current]
            for neighbour in neighbours:
                if visited.get(neighbour):
                    continue
                stack.append(neighbour)
                visited[neighbour] = True
