from collections import deque
from typing import Optional
from structures import TreeNode


class TreeBuilder:
    @staticmethod
    def from_list(values: list[Optional[int]]) -> Optional[TreeNode]:
        if not values or values[0] is None:
            return None

        root = TreeNode(values[0])
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1

            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1

        return root
