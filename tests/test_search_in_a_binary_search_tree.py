import pytest
from src.binary_search_tree.search_in_a_binary_search_tree.solution import Solution
from test_utils import TreeBuilder


@pytest.mark.parametrize(
    "root, val, expected",
    [([4, 2, 7, 1, 3], 2, [2, 1, 3]), ([4, 2, 7, 1, 3], 5, [])],
)
def test_search_bst(root, val, expected):
    root = TreeBuilder.from_list(root)
    solution = Solution()
    assert TreeBuilder.to_list(solution.searchBST(root, val)) == expected
