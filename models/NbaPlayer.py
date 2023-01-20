from dataclasses import dataclass
from functools import total_ordering

@dataclass
@total_ordering
class NbaPlayer:
    slug: str
    team: str
    isActive: bool
    latestThreeFixtureStats: int
    latestFiveFixtureStats: int
    tenGameAverage: int
    latestThreeFixtureStatsDiff: int
    latestFiveFixtureStatsDiff: int

    def __init__(self, slug: str, team: str, isActive: bool, latestThreeFixtureStats: int, latestFiveFixturesStats: int, tenGameAverage: int):
        self.slug = slug
        self.team = team
        self.isActive = isActive
        self.latestThreeFixtureStats = latestThreeFixtureStats
        self.latestFiveFixtureStats = latestFiveFixturesStats
        self.tenGameAverage = tenGameAverage
        self.latestThreeFixtureStatsDiff = self.__performanceLastThreeDiff()
        self.latestFiveFixtureStatsDiff = self.__performanceLastFiveDiff()

    def __performanceLastThreeDiff(self) -> int:
        return self.latestThreeFixtureStats - self.tenGameAverage
        
    def __performanceLastFiveDiff(self) -> int:
        return self.latestFiveFixtureStats - self.tenGameAverage

    def _is_valid_operand(self, other):
        return hasattr(other, "latestThreeFixtureStatsDiff")

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.slug == other.slug

    def __gt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.latestThreeFixtureStatsDiff > other.latestThreeFixtureStatsDiff