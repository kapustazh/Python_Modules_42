from ex0.Card import Card
from ex2.Magical import Magical
from ex2.Combatable import Combatable


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str,
                 cost: int,
                 rarity: str, damage: int, health: int, combat_type: str):
        super().__init__(name, cost, rarity)
        self.combat_type: str = combat_type
        self.damage: int = damage
        self.health: int = health

    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.damage,
            "combat_type": self.combat_type,
        }

    def defend(self, incoming_damage: int) -> dict: ...

    def get_combat_stats(self) -> dict:
        return {"combat_type": self.combat_type}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    def channel_mana(self, amount: int) -> dict:
        pass

    def get_magic_stats(self) -> dict:
        pass
