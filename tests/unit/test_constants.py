from cloudprice.constants import Enum


class TestEnum(object):
    def test_mixed_case(self):
        Seasons = Enum(season_SPRING="Spring", season_AUTUMN="Autumn")
        assert Seasons.SEASON_SPRING == "Spring"
        assert "Spring" in Seasons.values()
