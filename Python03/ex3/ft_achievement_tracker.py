def ft_achievement_tracker() -> None:
    """Achievement tracker manager that provides
        brief statistics of each player's
        achievements
    """
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter',
               'boss_slayer', 'speed_demon', 'perfectionist'}
    print("=== Achievement Tracker System ===")
    print()
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print()
    print("=== Achievement Analytics ===")
    players = [bob, charlie, alice]
    unique_achievements = set.union(*players)
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print()
    common_achievements = set.intersection(*players)
    print(f"Common to all players: {common_achievements}")
    rare_achievements = (
        (bob - (charlie | alice)) |
        (charlie - (bob | alice)) |
        (alice - (bob | charlie))
    )
    print("Rare achievements (1 player): ", rare_achievements)
    print()
    alice_vs_bob = alice.intersection(bob)
    print("Alice vs Bob common:", alice_vs_bob)
    alice_unique = alice.difference(bob)
    print("Alice unique:", alice_unique)
    bob_unique = bob.difference(alice)
    print("Bob unique:", bob_unique)


if __name__ == "__main__":
    ft_achievement_tracker()
