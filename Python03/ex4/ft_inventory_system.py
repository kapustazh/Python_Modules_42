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
            armor += stats.get("quantity")
        elif stats["type"] == "consumable":
            consumable += stats.get("quantity")

    print(f"Categories: weapon({weapons})" f",consumable({consumable}) armor({armor})")
    print("=== Transaction: Alice gives Bob 2 potions ===")
    alice_inventory["potion"]["quantity"] -= 2
    if "potion" in bob_inventory:
        bob_inventory["potion"]["quantity"] += 2
    else:
        bob_inventory["potion"] = {
            "type": "consumable",
            "rarity": "common",
            "price": 50,
            "quantity": 2,
        }
    print("Transaction successful!")
    print()
    print("=== Updated Inventories ===")
    print(f"Alice potions: {alice_inventory["potion"].get("quantity")}")
    print(f"Bob potions: {bob_inventory["potion"].get("quantity")}")
    print()

    alice_price = 0
    alice_count = 0
    for item_name, stats in alice_inventory.items():
        alice_price += stats["quantity"] * stats["price"]
        alice_count += stats["quantity"]  # Summing for total items (7), not max stack

    bob_price = 0
    bob_count = 0
    for item_name, stats in bob_inventory.items():
        bob_price += stats["quantity"] * stats["price"]
        bob_count += stats["quantity"]

    if alice_price > bob_price:
        name = "Alice"
        mvp_gold = alice_price
        most_items = alice_count

        rarest_items = [
            item_name
            for item_name, stats in alice_inventory.items()
            if stats["rarity"] == "rare"
        ]
    else:
        name = "Bob"
        mvp_gold = bob_price
        most_items = bob_count

        rarest_items = [
            item_name
            for item_name, stats in bob_inventory.items()
            if stats["rarity"] == "rare"
        ]

    rarest_items = []
    for item_name, stats in alice_inventory.items():
        if stats["rarity"] == "rare":
            rarest_items.append(item_name)
    for item_name, stats in bob_inventory.items():
        if stats["rarity"] == "rare":
            rarest_items.append(item_name)

    print("Rarest items:", end=" ")
    print(*rarest_items, sep=", ")


if __name__ == "__main__":
    ft_inventory_system()

# dict(), len(), print(), keys(), values(), items(), get(),
# update()
