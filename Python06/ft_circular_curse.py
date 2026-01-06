from alchemy.grimoire import validate_ingredients, record_spell


def ft_circular_curse() -> None:
    """Demo to test late import"""
    try:
        print("=== Circular Curse Breaking ===")
        print()
        print("Testing ingredient validation:")

        fire_air = validate_ingredients("fire air")
        print('validate_ingredients("fire air"):', fire_air)
        dragon_scales = validate_ingredients("dragon scales")
        print('validate_ingredients("dragon scales"):', dragon_scales)
        print()
        print("Testing spell recording with validation:")
        fireball = record_spell("Fireball", "fire air")
        print('record_spell("Fireball", "fire air"):', fireball)
        dark_magic = record_spell("Dark Magic", "shadow")
        print('record_spell("Dark Magic", "shadow"):', dark_magic)
        print()
        # why would i test this

        lightning = record_spell("Lightning", "air")
        print("Testing late import technique:")
        print('record_spell("Lightning", "air"):', lightning)
        print()
        print("Circular dependency curse avoided using late imports!")
        print("All spells processed safely!")
    except Exception as e:
        print(f"Something went wrong -> {e}")


if __name__ == "__main__":
    ft_circular_curse()
