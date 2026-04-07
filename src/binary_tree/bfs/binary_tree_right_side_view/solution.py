from typing import Optional, List
from collections import deque
from structures import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = deque()
        q.append(root)

        while q:
            right_side = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    right_side = node
                    q.append(node.left)
                    q.append(node.right)
            if right_side:
                result.append(right_side.val)
        return result
