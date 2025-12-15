def ft_garden_intro():
    """Demo routine that prints a simple plant introduction.

    Sets up minimal plant attributes (name, height, age) and prints them
    to demonstrate a basic plant summary output.
    """
    flower_name: str = "Sunflower"
    flower_height: int = 20
    flower_age: int = 15
    info = (
        f"Plant: {flower_name}\n"
        f"Height: {flower_height}\n"
        f"Age: {flower_age}\n"
    )
    print("=== End of Program ===")
    print(info)


if __name__ == "__main__":
    ft_garden_intro()
