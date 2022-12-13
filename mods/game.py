from dataclasses import dataclass
from pandas import DataFrame


@dataclass
class Game:
    info: dict[str, str]
    tables: dict[str, DataFrame]
