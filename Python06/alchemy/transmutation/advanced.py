from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """Returns philosopher's stone"""
    return (
        f"Philosopher’s stone created using "
        f"{lead_to_gold()} and {healing_potion()}"
    )


def elixir_of_life() -> str:
    """Returns elixir of life"""
    return "Elixir of life: eternal youth achieved!"
