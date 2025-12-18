import sys


def ft_command_quest() -> None:
    print("=== Command Quest ===")
    if len(sys.argv) < 2:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) > 1:
        print(f"Arguments recieved: {len(sys.argv) - 1}")
    count = 1
    for arg in sys.argv[1:]:
        print(f"Argument {count}: {arg}")
        count += 1
    print(f"Total arguments: {len(sys.argv)}")
    # Authorized: import sys, sys.argv, len(), print()


if __name__ == "__main__":
    ft_command_quest()
