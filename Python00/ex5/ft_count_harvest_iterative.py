def ft_count_harvest_iterative():
    daysUntilHarvest = int(input("Days until harvest: "))

    for currentDay in range(1, daysUntilHarvest + 1):
        print(f"Day {currentDay}")

    print("Harvest time!")
