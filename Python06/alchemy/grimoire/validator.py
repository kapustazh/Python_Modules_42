def validate_ingredients(ingredients: str) -> str:
    """Function that validates ingrdients

    Args:
        ingredients (str): components of potions

    Returns:
        str: validity of ingredients
    """
    if any(elem in ingredients for elem in ("fire", "water", "earth", "air")):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
