from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_queue = deque()
        dire_queue = deque()

        length = len(senate)

        for i in range(length):
            if senate[i] == "R":
                radiant_queue.append(i)
            else:
                dire_queue.append(i)

        while radiant_queue and dire_queue:
            radiant = radiant_queue.popleft()
            dire = dire_queue.popleft()

            if radiant < dire:
                radiant_queue.append(radiant + length)
            else:
                dire_queue.append(dire + length)

        return "Radiant" if radiant_queue else "Dire"
