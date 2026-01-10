from ex0.Card import Card


class SpellCard(Card):
    """SpellCard class, represents a spell card with effect type"""
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type

    def play(self, game_state: dict) -> dict:
        """Method to play the spell card"""
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect_type
        }

    def resolve_effect(self, targets: list) -> dict:
        """Resolve the spell's effect on targets

        Args:
            targets (list): list of targets

        Returns:
            dict: effect result
        """
        return {
            'effect': self.effect_type,
            'targets': targets
        }
