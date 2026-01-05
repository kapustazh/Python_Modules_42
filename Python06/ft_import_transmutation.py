import alchemy.elements
from alchemy.elements import create_water
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_earth, create_fire
from alchemy.potions import strength_potion


def ft_import_transmutation() -> None:
    """Demo function to test different types of import"""
    try:
        print("=== Import Transmutation Mastery ===")
        print()
        # import alchemy.elements

        print("Method 1 - Full module import:")
        fire = alchemy.elements.create_fire()
        print(f"alchemy.elements.create_fire(): {fire}")
        print()
        # from alchemy.elements import create_water

        print("Method 2 - Specific function import:")
        print(f"create_water(): {create_water()}")
        print()
        # from alchemy.potions import healing_potion as heal

        print("Method 3 - Aliased import:")
        print(f"heal(): {heal()}")
        print()
        # from alchemy.elements import create_earth, create_fire
        # from alchemy.potions import strength_potion

        print("Method 4 - Multiple imports:")
        print("create_earth():", create_earth())
        print("create_fire():", create_fire())
        print("strength_potion():", strength_potion())
        print("All import transmutation methods mastered!")
    except Exception as e:
        print(f"Something went wrong -> {e}")


if __name__ == "__main__":
    ft_import_transmutation()
