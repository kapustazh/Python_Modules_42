def record_spell(spell_name: str, ingredients: str) -> str:
    """Recoreds the spell and validates them

    Returns:
        str: Either records or rejects the spell
        if it's valid or not
    """
    from .validator import validate_ingredients

    is_valid = validate_ingredients(ingredients)
    if "VALID" in is_valid:
        return f"Spell recorded: {spell_name} ({is_valid})"
    else:
        return f"Spell rejected: {spell_name} ({is_valid})"
