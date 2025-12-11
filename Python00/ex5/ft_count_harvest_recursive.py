def ft_count_harvest_recursive():
    def recursion(*, currentDay: int):
        if currentDay == daysUntilHarvest + 1:
            print("Harvest time!")
            return
        print(f"Day {currentDay}")
        currentDay += 1
        recursion(currentDay=currentDay)
    daysUntilHarvest = int(input("Days until harvest: "))
    currentDay = 1
    recursion(currentDay=currentDay)
