from collections import deque
from typing import Optional
from structures import TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        curr_lvl = 1
        maximum = float("-inf")
        ans = 1
        queue = deque([root])

        while queue:
            curr_sum = 0
            lvl_size = len(queue)
            for _ in range(lvl_size):
                node = queue.popleft()
                curr_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if curr_sum > maximum:
                maximum = curr_sum
                ans = curr_lvl
            curr_lvl += 1
        return ans
