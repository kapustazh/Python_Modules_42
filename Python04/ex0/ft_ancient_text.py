def ft_ancient_text() -> None:
    """Function that reads file and prints it's data"""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")

    try:
        file = open("ancient_fragment.txt", "r")

        print("Connection established...\n")
        print("RECOVERED DATA:")

        print(file.read())

        file.close()

        print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found")


if __name__ == "__main__":
    ft_ancient_text()
