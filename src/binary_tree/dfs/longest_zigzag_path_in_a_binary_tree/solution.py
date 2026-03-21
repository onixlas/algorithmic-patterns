from typing import Optional
from structures import TreeNode


class Solution:
    def dfs(
        self, root: Optional[TreeNode], prev_direction: str, cur_length: int
    ) -> int:
        if root is None:
            return cur_length - 1
        if prev_direction == "left":
            right_length = self.dfs(root.right, "right", cur_length + 1)
            left_length = self.dfs(root.left, "left", 1)
        else:
            right_length = self.dfs(root.right, "right", 1)
            left_length = self.dfs(root.left, "left", cur_length + 1)
        return max(left_length, right_length)

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        right_length = self.dfs(root.right, "right", 1)
        left_length = self.dfs(root.left, "left", 1)
        return max(right_length, left_length)
