import pytest
from src.graphs.number_of_provinces.solution import Solution


@pytest.mark.parametrize(
    "isConnected, expected",
    [([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2), ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3)],
)
def test_number_of_provinces(isConnected, expected):
    solution = Solution()
    assert solution.findCircleNum(isConnected) == expected
