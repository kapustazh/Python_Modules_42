def healing_potion() -> str:
    """Returns string with heal potion"""
    from .elements import create_fire, create_water

    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    """Returns string with strength potion"""
    from .elements import create_earth, create_fire

    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    """Returns string with invis potion"""
    from .elements import create_air, create_water

    return (
        f"Invisibility potion brewed with {create_air()} and {create_water()}"
    )


def wisdom_potion() -> str:
    """Returns string with wisdom potion"""
    from .elements import create_air, create_water, create_earth, create_fire

    message = [create_air(), create_water(), create_earth(), create_fire()]
    all_four = " ".join(message)
    return f"Wisdom potion brewed with all elements: {all_four}"
