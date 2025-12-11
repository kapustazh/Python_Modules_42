def ft_plant_age():
    plantAge = int(input("Enter plant age in days: "))
    if plantAge > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
