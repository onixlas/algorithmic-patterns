import pytest
from src.binary_tree.bfs.maximum_level_sum_of_a_binary_tree.solution import Solution
from test_utils import TreeBuilder


@pytest.mark.parametrize(
    "root, expected",
    [
        ([1, 7, 0, 7, -8, None, None], 2),
        ([989, None, 10250, 98693, -89388, None, None, None, -32127], 2),
    ],
)
def test_max_depth(root, expected):
    root = TreeBuilder.from_list(root)
    solution = Solution()
    assert solution.maxLevelSum(root) == expected
