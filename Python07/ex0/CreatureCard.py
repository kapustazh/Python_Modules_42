from ex0.Card import Card


class CreatureCard(Card):

    def __init__(self, name: str,
                 cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: dict) -> dict:
        return game_state | {
            'name': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

    def attack_target(self, target) -> dict:
        print(self.name, "attacks", target.name)
        if self.attack >= target.health:
            status = True
        else:
            status = False
        return {
            'attacker': self.name,
            'target': target.name,
            'combat_resolved': status
        }
