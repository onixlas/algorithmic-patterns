class Solution:
    def dfs(
        self,
        adjacent: list[list[tuple[int, int]]],
        visited: list[bool],
        current_city: int,
    ) -> int:
        visited[current_city] = True
        changes = 0
        for neighbour, direction in adjacent[current_city]:
            if not visited[neighbour]:
                if direction == 1:
                    changes += 1
                changes += self.dfs(adjacent, visited, neighbour)

        return changes

    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        adjacent = [[] for _ in range(n)]
        for u, v in connections:
            adjacent[u].append((v, 1))
            adjacent[v].append((u, -1))
        visited = [False] * n
        return self.dfs(adjacent, visited, 0)
