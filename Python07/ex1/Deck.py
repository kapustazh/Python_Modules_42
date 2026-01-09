from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class Deck():
    deck: list = []

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.deck:
            if card.name == card_name:
                self.deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        card_to_draw: Card = self.deck.pop()
        return card_to_draw

    def get_deck_stats(self) -> dict:
        total_cost: int = sum(card.cost for card in self.deck)
        count: int = len(self.deck)
        avg_cost: float = total_cost / count if count > 0 else 0
        return {
            'total_cards': len(self.deck),
            'creatures': sum(
                isinstance(card, CreatureCard) for card in self.deck
            ),
            'spells': sum(isinstance(card, SpellCard) for card in self.deck),
            'artifacts': sum(
                isinstance(card, ArtifactCard) for card in self.deck
            ),
            'avg_cost': avg_cost
        }
