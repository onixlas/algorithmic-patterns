import pytest
from src.binary_tree.dfs.longest_zigzag_path_in_a_binary_tree.solution import Solution
from test_utils import TreeBuilder


@pytest.mark.parametrize(
    "root, expected",
    [
        ([1, None, 2, 3, 4, None, None, 5, 6, None, 7, None, None, None, 8], 3),
        ([1, 1, 1, None, 1, None, None, 1, 1, None, 1], 4),
        ([1], 0),
    ],
)
def test_max_depth(root, expected):
    root = TreeBuilder.from_list(root)
    solution = Solution()
    assert solution.longestZigZag(root) == expected
