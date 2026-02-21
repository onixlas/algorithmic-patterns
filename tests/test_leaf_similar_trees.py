import pytest
from src.binary_tree.dfs.leaf_similar_trees.solution import Solution
from test_utils import TreeBuilder


@pytest.mark.parametrize(
    "root1, root2, expected",
    [
        (
            [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4],
            [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8],
            True,
        ),
        ([1, 2, 3], [1, 3, 2], False),
    ],
)
def test_leaf_similar(root1: list, root2: list, expected: bool):
    root1 = TreeBuilder.from_list(root1)
    root2 = TreeBuilder.from_list(root2)
    solution = Solution()
    assert solution.leafSimilar(root1, root2) == expected
