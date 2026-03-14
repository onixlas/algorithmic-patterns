from typing import Optional
from collections import defaultdict
from structures import TreeNode


class Solution:
    def dfs(self, root: Optional[TreeNode], current_sum: int, target_sum: int):
        if root is None:
            return 0

        current_sum += root.val
        count: int = self.cache[current_sum - target_sum]
        self.cache[current_sum] += 1

        count += self.dfs(root.left, current_sum, target_sum)
        count += self.dfs(root.right, current_sum, target_sum)

        self.cache[current_sum] -= 1

        return count

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.cache = defaultdict(int)
        self.cache[0] = 1
        return self.dfs(root, 0, targetSum)
