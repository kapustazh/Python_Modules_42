from ex0.Card import Card
import random


class Deck():
    deck: list[Card] = []

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
        return {}
