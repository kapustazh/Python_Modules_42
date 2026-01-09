from ex0.CreatureCard import CreatureCard


def main() -> None:
    try:
        print("=== DataDeck Card Foundation ===")
        print()
        print("Testing Abstract Base Class Design:")
        print()
        current_mana: int = 10
        fire_dragon: CreatureCard = CreatureCard(
            "Fire Dragon", 5, "Legendary", 7, 5)
        print("CreatureCard Info:")
        print(fire_dragon.get_card_info())
        print()
        print(f"Plaing {fire_dragon.name} with {current_mana} mana available")
        print("Playable:", fire_dragon.is_playable(current_mana))
        print("Play result:", fire_dragon.play({}))
        current_mana -= fire_dragon.cost
        print()
        goblin_warrior: CreatureCard = CreatureCard(
            "Goblin Warrior", 2, "common", 1, 1)
        print(fire_dragon.attack_target(goblin_warrior))
        print()
        print(f"Testing insufficient mana ({current_mana} available):")
        print("Playable:", fire_dragon.is_playable(current_mana))
        print()
        print("Abstract pattern successfully demonstrated!")
    except Exception as e:
        print(f"Something went wrong -> {e}")


if __name__ == "__main__":
    main()
