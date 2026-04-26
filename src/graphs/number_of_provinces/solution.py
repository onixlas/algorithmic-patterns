class Solution:
    def dfs(self, node: int, isConnected: list[list[int]], visited: list[bool]):
        visited[node] = True
        for i in range(len(isConnected)):
            if isConnected[node][i] and not visited[i]:
                self.dfs(i, isConnected, visited)

    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        provinces = 0
        visited = [False] * len(isConnected)
        for i in range(len(isConnected)):
            if not visited[i]:
                provinces += 1
                self.dfs(i, isConnected, visited)
        return provinces
