import alchemy.elements
import alchemy


def ft_sacred_scroll() -> None:
    """Demo to show import"""
    print("=== Sacred Scroll Mastery ===")
    print()
    print("Testing direct module access:")
    fire = alchemy.elements.create_fire()
    water = alchemy.elements.create_water()
    earth = alchemy.elements.create_earth()
    air = alchemy.elements.create_air()
    print(f"alchemy.elements.create_fire(): {fire}")
    print(f"alchemy.elements.create_water(): {water}")
    print(f"alchemy.elements.create_earth(): {earth}")
    print(f"alchemy.elements.create_fire(): {air}")
    print()
    print("Testing package-level access (controlled by __init__.py):")
    fire = alchemy.create_fire()
    water = alchemy.create_water()
    print(f"alchemy.create_fire(): {fire}")
    print(f"alchemy.create_water(): {water}")
    print("alchemy.create_earth(): ", end="")
    try:
        earth = alchemy.create_earth()
        print(earth)
    except AttributeError:
        print("AttributeError - not exposed")
    print("alchemy.create_air(): ", end="")
    try:
        air = alchemy.create_air()
        print(air)
    except AttributeError:
        print("AttributeError - not exposed")

    print()
    print("Package metadata:")
    print("Version:", alchemy.__version__)
    print("Author:", alchemy.__author__)


if __name__ == "__main__":
    ft_sacred_scroll()
