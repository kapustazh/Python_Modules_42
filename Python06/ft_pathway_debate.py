from alchemy.transmutation import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life
import alchemy


def ft_pathway_debate() -> None:
    """Demo to test relative and absolute import of modules"""
    print("=== Pathway Debate Mastery ===")
    print()
    print("Testing Absolute Imports (from basic.py):")
    print("lead_to_gold():", lead_to_gold())
    print("stone_to_gem():", stone_to_gem())
    print()
    print("Testing Relative Imports (from advanced.py):")
    print("philosophers_stone():", philosophers_stone())
    print("elixir_of_life():", elixir_of_life())
    print()
    print("Testing Package Access:")
    lead_to_gold_msg = alchemy.transmutation.lead_to_gold()
    print("alchemy.transmutation.lead_to_gold():", lead_to_gold_msg)
    philosophers_msg = alchemy.transmutation.philosophers_stone()
    print("alchemy.transmutation.philosophers_stone():", philosophers_msg)
    print()
    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    ft_pathway_debate()
