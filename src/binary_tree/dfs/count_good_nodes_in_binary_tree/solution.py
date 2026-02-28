from structures import TreeNode


class Solution:
    def good_w_max(self, cur_max, root: TreeNode) -> int:
        if root:
            counter = 0
            if root.val >= cur_max:
                counter += 1
            cur_max = max(cur_max, root.val)
            return (
                counter
                + self.good_w_max(cur_max, root.left)
                + self.good_w_max(cur_max, root.right)
            )
        return 0

    def goodNodes(self, root: TreeNode) -> int:
        return (
            1
            + self.good_w_max(root.val, root.left)
            + self.good_w_max(root.val, root.right)
        )
