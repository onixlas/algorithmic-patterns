import pytest
from src.graphs.keys_and_rooms.solution import Solution


@pytest.mark.parametrize(
    "rooms, expected",
    [([[1], [2], [3], []], True), ([[1, 3], [3, 0, 1], [2], [0]], False)],
)
def test_keys_and_rooms(rooms, expected):
    solution = Solution()
    assert solution.canVisitAllRooms(rooms) == expected
