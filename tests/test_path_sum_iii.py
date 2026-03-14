import pytest
from src.binary_tree.dfs.path_sum_iii.solution import Solution
from test_utils import TreeBuilder


@pytest.mark.parametrize(
    "root, target_sum, expected",
    [
        ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, 3),
    ],
)
def test_leaf_similar(root: list, target_sum: int, expected: int):
    root = TreeBuilder.from_list(root)
    solution = Solution()
    assert solution.pathSum(root, target_sum) == expected
