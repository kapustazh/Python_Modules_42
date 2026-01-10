from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class Deck():
    """Deck class, manages a collection of cards"""
    deck: list = []

    def add_card(self, card: Card) -> None:
        """Add a card to the deck

        Args:
            card (Card): the card to add
        """
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a card from the deck by name

        Args:
            card_name (str): name of the card to remove

        Returns:
            bool: True if card was removed, False otherwise
        """
        for card in self.deck:
            if card.name == card_name:
                self.deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Shuffle the deck"""
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        """Draw a card from the deck

        Returns:
            Card: the drawn card
        """
        card_to_draw: Card = self.deck.pop()
        return card_to_draw

    def get_deck_stats(self) -> dict:
        """Get statistics about the deck

        Returns:
            dict: dictionary with deck statistics
        """
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
