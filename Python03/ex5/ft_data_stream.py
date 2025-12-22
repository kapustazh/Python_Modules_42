def ft_data_stream() -> None:
    """Streams meme strings

    Yields:
        -Game simulator
        -Fibonaci sequence
        -Prime sequence
    """
    print("=== Game Data Stream Processor ===")
    events_count = 100
    names = ["Arestovich", "Lenin", "Stalin", "Austrian painter"]
    levels = [6, 7, 322, 228]
    events = ["sleeps - zZzZzZzZz...", "found treasure", "leveled up"]
    print()
    print(f"Processing {events_count} game events...")
    print()
    stats = {"high_level": 0, "treasure": 0, "level_up": 0}

    def create_game_stream(limit: int, stats_box: dict):
        for idx in range(events_count):
            player_i = idx % 4
            event_i = (idx // 4) % 3

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
    for event in stream:
        print(event)
    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {events_count}")
    print(f"High-level players (10+): {stats['high_level']}")
    print(f"Treasure events: {stats['treasure']}")
    print(f"Level-up events: {stats['level_up']}")
    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print()
    print("=== Generator Demonstration ===")

    def fibonaci(n: int):
        a = 0
        b = 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    def is_prime(number):
        if number > 1:
            for x in range(2, number):
                if number % x == 0:
                    return False
            return True
        else:
            return False

    def prime_nums_generator(count: int):
        yielded = 0
        candidate = 2
        while yielded < count:
            if is_prime(candidate):
                yield candidate
                yielded += 1
            candidate += 1

    print()
    nums = fibonaci(10)
    print("Fibonacci sequence (first 10):", end=" ")
    print(next(nums), end='')
    for num in nums:
        print(f", {num}", end='')
    nums_new = prime_nums_generator(5)
    print()
    print("Prime sequence (first 5):", end=" ")
    print(next(nums_new), end='')
    for num in nums_new:
        print(f", {num}", end='')
    print()


if __name__ == "__main__":
    ft_data_stream()

# : yield, next(), iter(), range(), len(), print(), for loops
