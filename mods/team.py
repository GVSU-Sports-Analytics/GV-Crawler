from dataclasses import dataclass, field
from player import Player


@dataclass
class Team:
	name: str
	players: list[Player] = field(default_factory=lambda: [])
	
