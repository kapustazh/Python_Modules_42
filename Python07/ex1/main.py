from ex0.Card import Card


from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard


def main() -> None:
    try:
        print("=== DataDeck Deck Builder ===")
        print()
        my_deck: Deck = Deck()
        lightning_bolt: SpellCard = SpellCard(
            "Lightning Bolt", 3, "rare",
            'Deal 3 damage to target')
        mana_crystal: ArtifactCard = ArtifactCard(
            "Mana Crystal", 2, "common", 5, "Permanent: +1 mana per turn"
        )
        fire_dragon: CreatureCard = CreatureCard(
            "Fire Dragon", 5, "Legendary", 7, 5)
        for card_to_add in (lightning_bolt, mana_crystal, fire_dragon):
            my_deck.add_card(card=card_to_add)
        my_deck.shuffle()
        print("Drawing and playing cards:")
        while len(my_deck.deck) > 0:
            card: Card = my_deck.draw_card()
            card_data: dict = card.get_card_info()
            print(f"Drew: {card.name} ({card_data['type']})")
            print("Play result:", card.play({}))
            print()
        print("Building deck with different card types...")
    except Exception as e:
        print(f"Something went wrong -> {e}")


if __name__ == "__main__":
    main()
