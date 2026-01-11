from typing import Any


from ex2.EliteCard import EliteCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card


def main() -> None:
    print("=== DataDeck Ability System ===")
    print()
    print(EliteCard.__qualname__, "capabilities:")
    card_methods: list[Any] = [
        meth
        for meth in dir(Card)
        if callable(getattr(Card, meth)) and not meth.startswith("__")
    ]
    combatable_methods: list[Any] = [
        meth
        for meth in dir(Combatable)
        if callable(getattr(Combatable, meth)) and not meth.startswith("__")
    ]
    magical_methods: list[Any] = [
        meth
        for meth in dir(Magical)
        if callable(getattr(Magical, meth)) and not meth.startswith("__")
    ]
    print("- Card:", card_methods)
    print("- Combatable:", combatable_methods)
    print("- Magical:", magical_methods)
    arcane_warrior1: EliteCard = EliteCard(
        'Arcane warrior', 2, 'rare', 5, 10, 'melee'
    )
    arcane_warrior2: EliteCard = EliteCard(
        'Arcane warrior', 2, 'rare', 5, 10, 'melee'
    )
    print("Combat phase:")
    print()
    print("Attack result:", arcane_warrior1.attack(arcane_warrior2))


if __name__ == "__main__":
    main()
