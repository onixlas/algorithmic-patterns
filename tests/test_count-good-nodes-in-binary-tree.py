import pytest
from src.binary_tree.dfs.count_good_nodes_in_binary_tree.solution import Solution
from test_utils import TreeBuilder


@pytest.mark.parametrize(
    "root, expected",
    [([3, 1, 4, 3, None, 1, 5], 4), ([3, 3, None, 4, 2], 3), ([1], 1)],
)
def test_max_depth(root, expected):
    root = TreeBuilder.from_list(root)
    solution = Solution()
    assert solution.goodNodes(root) == expected
