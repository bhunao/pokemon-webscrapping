from dataclasses import dataclass

@dataclass
class Pokemon:
    id: int
    name: str
    type: str
    total: int
    hp: int
    attack: int
    defense: int
    sp_attack: int
    sp_defense: int
    speed: int
    sprite: str
