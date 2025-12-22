def ft_analytics_dashboard() -> None:
    """Analytics simulator which shows the work of
    list, dict and set comprehensions
    """
    people = {
        'stalin': {
            'score': 911,
            'achievements': {
                "first blood", "rampage", "ultra kill"
            },
            'region': "north",
            'activity': "active"
        },
        'lenin': {
            'score': 1441,
            'achievements': {
                "first blood", "ultra kill"
            },
            'region': "east",
            'activity': "passive"
        },
        'austrian painter': {
            'score': 42,
            'achievements': {
                "first blood", "stay alive while not moving for 10 minutes"
            },
            'region': "central",
            'activity': "active"
        },
        'arestovich': {
            'score': 6767,
            'achievements': {
                "first blood",
            },
            'region': "central",
            'activity': "passive"
        }
    }
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    print(
        "High scores (>2000):",
        [name for name in people if people[name]['score'] > 2000]
    )
    print(
        "Scores doubled:",
        [
            people[name]['score'] * 2
            for name in people if people[name]['score']
        ]
    )
    print(
        "Active players:",
        [
            name
            for name in people if people[name]['activity'] == "active"
        ]
    )
    print()
    print("=== Dict Comprehension Examples ===")
    print(
        "Player scores:",
        {name: people[name]['score'] for name in people}
    )
    print(
        "Score categories:",
        {category: sum
         (1 for name in people if
          (category == "high" and people[name]['score'] > 2000) or
          (category == "medium" and 1000 < people[name]['score'] <= 2000) or
          (category == "low" and people[name]['score'] <= 1000))
            for category in ["high", "medium", "low"]}
    )
    print(
        "Achievement counts:",
        {name: len(people[name]['achievements'])
            for name in people if people[name]['achievements']
         }
    )
    print()
    list_of_people = ["lenin", "stalin", "trump", "biden", "lenin", "biden"]
    print("=== Set Comprehension Examples ===")
    print(
        "Unique players:",
        {name for name in list_of_people}
    )
    print(
        "Unique achievements:",
        {achievement for name in people
         for achievement in people[name]['achievements']}
    )
    print(
        "Active regions:",
        {people[name]['region'] for name in people}
    )
    print()
    print("=== Combined Analysis ===")
    print("Total players:", len(people))
    print(
        "Total unique achievements:",
        len({achievement for name in people
             for achievement in people[name]['achievements']})
    )
    print(
        "Average score",
        sum([people[name]['score'] for name in people]) /
        len([people[name]['score'] for name in people])
    )
    top_score, top_name = max((people[name]['score'], name) for name in people)
    print(
        "Top performer:",
        top_name,
        f"({top_score} points, {len(people[top_name]['achievements'])}"
        f" achievements)"
    )


if __name__ == "__main__":
    ft_analytics_dashboard()

# List/dict/set comprehensions, len(), print(), sum(), max(),
# min(), sorted()
