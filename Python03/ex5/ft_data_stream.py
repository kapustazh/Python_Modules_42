def ft_data_stream():
    print("=== Game Data Stream Processor ===")
    events_count = 100
    names = ["alice", "bob", "charlie"]
    levels = [5, 8, 12]
    events = ["killed monster", "found treasure", "leveled up"]
    print()
    print(f"Processing {events_count} game events...")
    print()
    stats = {"high_level": 0, "treasure": 0, "level_up": 0}

    def create_game_stream(limit, stats_box) -> None:
        for idx in range(events_count):
            player_i = idx % 3
            dice_roll = (idx * 53 + 7) % 100

            if dice_roll < 70:
                event_i = 0
            elif dice_roll < 90:
                event_i = 1
            else:
                event_i = 2
            if events[event_i] == "leveled up":
                levels[player_i] += 1
                stats["level_up"] += 1

            if levels[player_i] >= 10:
                stats["high_level"] += 1

            if events[event_i] == "found treasure":
                stats["treasure"] += 1
            yield (
                f"Event {idx + 1}: Player {names[player_i]} "
                f"(level {levels[player_i]}) {events[event_i]}"
            )

    stream = create_game_stream(events_count, stats)
    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {events_count}")
    print(f"High-level players (10+): {stats["high_level"]}")
    print(f"Treasure events: {stats["treasure"]}")
    print(f"Level-up events: {stats["level_up"]}")


if __name__ == "__main__":
    ft_data_stream()

# : yield, next(), iter(), range(), len(), print(), for loops
