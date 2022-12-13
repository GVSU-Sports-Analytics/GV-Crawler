from dataclasses import dataclass
from pandas import DataFrame


@dataclass
class Game:
    opp_img: str
    info: dict[str, str]
    tables: dict[str, DataFrame]
