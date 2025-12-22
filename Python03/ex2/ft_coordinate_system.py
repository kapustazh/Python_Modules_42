import sys
from math import sqrt


def calculate_distance(pos1: tuple[int], pos2: tuple[int]) -> float:
    """Calculates the distance between two positions

    Args:
        pos1 (tuple[int]): coordinates of first position
        pos2 (tuple[int]): coordinates of second position

    Returns:
        float: distance
    """
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return sqrt((x2 - x1)**2 + (y2 - y1) ** 2 + (z2 - z1)**2)


def ft_coordinate_system() -> None:
    """Function which:
        -Takes coordinates of the player
        -Calculates distance of the player to start:
        -Demonstrates unpacking of tuples via
        showing position of players in the end
    """
    print("=== Game Coordinate System ===\n")
    pos_of_players = []
    pos1 = (10, 20, 5)
    start = (0, 0, 0)
    print(f"Position created: {pos1}")
    distance = calculate_distance(start, pos1)
    print(f"Distance {start} and {pos1}: {distance:.2f}\n")
    for arg in sys.argv[1:]:
        try:
            input_position = tuple(int(coord) for coord in arg.split(','))
            x, y, z = input_position
            pos_of_players += [input_position]
            print(f"Parsing coordinates: \"{x},{y},{z}\"")
            print(f"Parsed position: {input_position}")
            distance = calculate_distance(start, input_position)
            print(f"Distance {start} and {input_position}: {distance:.1f}\n")
        except Exception as e:
            print(
                f"Parsing invalid coordinates: \"{arg}\"\n"
                f"Error parsing coordinates:"
                f" invalid literal for int() with base 10:"
                f" '{arg}'")
            print(
                f"Error details - Type: "
                f"{type(e).__name__}, Args: (\"{e}\" )"
            )

    if pos_of_players:
        print("Unpacking demonstartion: ")
        for pos in pos_of_players:
            x, y, z = pos
            print(f"Player at x={x}, y={y}, z={z}")
            print(f"Coordinates: X={x}, Y={y}, Z={z}\n")


if __name__ == "__main__":
    ft_coordinate_system()

# Authorized: import sys, sys.argv, import math, tuple(), int(), float(),
# print(), split(), try/except, math.sqrt()
