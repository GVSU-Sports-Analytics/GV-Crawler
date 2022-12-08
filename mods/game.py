from dataclasses import dataclass


@dataclass
class Game:
    home_team: str
    away_team: str
    info: dict[str, str]
    pbp: dict[str, str]
    composite: dict[str, str]