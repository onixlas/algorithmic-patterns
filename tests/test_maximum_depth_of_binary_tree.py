import pytest
from src.binary_tree.dfs.maximum_depth_of_binary_tree.solution import Solution
from test_utils import TreeBuilder


@pytest.mark.parametrize(
    "root, expected",
    [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
    ],
)
def test_max_depth(root, expected):
    root = TreeBuilder.from_list(root)
    solution = Solution()
    assert solution.maxDepth(root) == expected
