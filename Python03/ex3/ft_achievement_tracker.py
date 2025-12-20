def ft_achievement_tracker() -> None:
    """Achevement tracker mannager, provides
        brief statistics of each player's
        achievments
    """
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter',
               'boss_slayer', 'speed_demon', 'perfectionist'}
    print("=== Achievement Tracker System ===")
    print()
    print(f"Player alice achievments: {alice}")
    print(f"Player bob achievments: {bob}")
    print(f"Player charlie achievments: {charlie}")
    print()
    print("=== Achievement Analytics ===")
    players = [bob, charlie, alice]
    unique_achievments = set.union(*players)
    print(f"All unique achievements:{unique_achievments}")
    print(f"Total unique achievements: {len(unique_achievments)}")
    print()
    common_achievments = set.intersection(*players)
    print(f"Common to all players: {common_achievments}")
    rare_achievements = (
        (bob - (charlie | alice)) |
        (charlie - (bob | alice)) |
        (alice - (bob | charlie))
    )
    print("Rare achievements (1 player): ", rare_achievements)
    print()
    alice_vs_bob = alice.intersection(alice)
    print("Alice vs Bob common:", alice_vs_bob)
    alice_unique = alice.difference(bob)
    print("Alice unique:", alice_unique)
    bob_unique = bob.difference(alice)
    print("Bob unique:", bob_unique)


if __name__ == "__main__":
    ft_achievement_tracker()
