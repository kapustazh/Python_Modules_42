def ft_inventory_system():
    print("=== Player Inventory System ===")
    print()
    alice_inventory = {
        "sword": {
            "type": 'weapon',
            "rarity": 'rare',
            "quantity": 1,
            "price": 500
        },
        "potion": {
            "type": "consumable",
            "rarity": "common",
            "quantity": 5,
            "price": 50
        },
        "shield": {
            "type": 'armor',
            "rarity": 'uncommon',
            "quantity": 1,
            "price": 200
        }
    }
    alice_inventory_price = 0
    counter_of_items = 0
    print("=== Alice's Inventory ===")
    for item_name, stats in alice_inventory.items():
        item_type = stats["type"]
        rarity = stats["rarity"]
        quantity = stats["quantity"]
        price = stats["price"]
        total_value = quantity * price
        alice_inventory_price += total_value
        counter_of_items += quantity
        print(f"{item_name} ({item_type}, {rarity}): {quantity}x @ {price}"
              f" gold each = {total_value} gold")
    print(f"Inventory value: {alice_inventory_price} gold")
    print(f"Item count: {counter_of_items}")
    weapons, consumable, armor = 0
    for item_name, stats in alice_inventory.items():
        if stats["type"] == "weapon":
            weapons += 1
        elif stats["type"] == "armor":
            armor += 1
        else:
            consumable += 1
    print(
        f"Categories: \"weapon\"({weapons})"
        ",\"consumable\"({consumable}) \"armor\"({armor})"
    )


if __name__ == "__main__":
    ft_inventory_system()

# dict(), len(), print(), keys(), values(), items(), get(),
# update()
