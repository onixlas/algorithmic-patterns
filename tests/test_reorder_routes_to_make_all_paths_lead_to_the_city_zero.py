import pytest
from src.graphs.reorder_routes_to_make_all_paths_lead_to_the_city_zero.solution import (
    Solution,
)


@pytest.mark.parametrize(
    "n, connecntions, expected",
    [
        (6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]], 3),
        (5, [[1, 0], [1, 2], [3, 2], [3, 4]], 2),
        (3, [[1, 0], [2, 0]], 0),
    ],
)
def test_min_reorder(n, connections, expected):
    solution = Solution()
    assert solution.minReorder(n, connections) == expected
