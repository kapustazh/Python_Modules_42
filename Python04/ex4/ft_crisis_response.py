def ft_crisis_response() -> None:
    """Function that tests FileNotFoundError, PermissionError"""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open("lost_archive.txt") as file:
            pass
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable")

    print()

    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open("classified_vault.txt", "a") as file:
            file.write("Hello")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, security maintained")

    print()

    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt") as file:
            print(f'SUCCESS: Archive recovered - "{file.read()}"')
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")

    print("STATUS: Normal operations resumed\n")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
