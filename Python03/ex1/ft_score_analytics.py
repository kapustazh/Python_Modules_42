import sys


def ft_score_analytics() -> None:
    """Fuction that takes scores as an input from terminal"""
    print("=== Player Score Analytics ===")
    list_of_scores = []
    for arg in sys.argv[1:]:
        try:
            value = int(arg)
            list_of_scores += [value]
        except ValueError:
            print(f"Ooops, '{arg}' is wrong type of the score :D")
    if len(list_of_scores) > 0:
        length = len(list_of_scores)
        sum_of_scores = sum(list_of_scores)
        print(f"Scores proccessed: {list_of_scores}")
        print(f"Total Players: {length}")
        print(f"Total score: {sum_of_scores}")
        print(f"Average score: {sum_of_scores / length}")
        print(f"High score: {max(list_of_scores)}")
        print(f"Low score: {min(list_of_scores)}")
        print(f"Score range: {max(list_of_scores) - min(list_of_scores)}")
    else:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py"
            " <score1> <score2> ...")


if __name__ == "__main__":
    ft_score_analytics()
