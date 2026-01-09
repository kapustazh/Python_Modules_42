from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str,
                 cost: int, rarity: str, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability: int = durability
        self.effect: str = effect

    def play(self, game_state: dict) -> dict:
        return {}

    def activate_ability(self) -> dict:
        return {}
