class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        while stack:
            node = stack.pop()
            for k in rooms[node]:
                if not seen[k]:
                    seen[k] = True
                    stack.append(k)
        return all(seen)
