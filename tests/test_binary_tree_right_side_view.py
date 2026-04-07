import pytest
from src.binary_tree.bfs.binary_tree_right_side_view.solution import Solution
from test_utils import TreeBuilder


@pytest.mark.parametrize(
    "root, expected",
    [
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
        ([1, 2, 3, 4, None, None, None, 5], [1, 3, 4, 5]),
        ([1, None, 3], [1, 3]),
        ([], []),
    ],
)
def test_max_depth(root, expected):
    root = TreeBuilder.from_list(root)
    solution = Solution()
    assert solution.rightSideView(root) == expected
