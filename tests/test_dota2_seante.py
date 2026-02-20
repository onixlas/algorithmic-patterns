import pytest
from src.queue.dota2_senate.solution import Solution


@pytest.mark.parametrize(
    "senate, expected",
    [
        ("RD", "Radiant"),
        ("RDD", "Dire")
    ],
)
def test_predict_party_victory(senate, expected):
    solution = Solution()
    assert solution.predictPartyVictory(senate) == expected