def ft_archive_creation() -> None:
    """Function that creates file and writes the data inside"""
    try:
        print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
        print("Initializing new storage unit: new_discovery.txt")
        file = open("new_discovery.txt", "w")
        print("Storage unit created successfully...\n")
        print(
            "Inscribing preservation data...\n"
            "[ENTRY 001] New quantum algorithm discovered\n"
            "[ENTRY 002] Efficiency increased by 347%\n"
            "[ENTRY 003] Archived by Data Archivist trainee\n"
        )
        file.write(
            "[ENTRY 001] New quantum algorithm discovered\n"
            "[ENTRY 002] Efficiency increased by 347%\n"
            "[ENTRY 003] Archived by Data Archivist trainee"
        )
        print(
            "Data inscription complete. Storage unit sealed.\n"
            "Archive 'new_discovery.txt' ready for long-term preservation."
        )
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found")


if __name__ == "__main__":
    ft_archive_creation()
