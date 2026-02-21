from structures import TreeNode
from itertools import zip_longest
from typing import Optional


class Solution:
    def get_leaves(self, root: TreeNode) -> list:
        if root:
            if not root.left and not root.right:
                yield [root.val]
            yield from self.get_leaves(root.right)
            yield from self.get_leaves(root.left)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        sentinel = object()
        return all(
            a == b
            for a, b in zip_longest(
                self.get_leaves(root1), self.get_leaves(root2), fillvalue=sentinel
            )
        )
