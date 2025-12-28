def ft_vault_security() -> None:
    """Function that opens file and appends text
    from other file to the end of the first one"""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    try:
        with open(
            "classified_data.txt",
            "r",
        ) as file:
            print("SECURE EXTRACTION:", file.read(), sep="\n")
            print()

        with open(
            "security_protocols.txt",
            "r",
        ) as file:
            text_to_write = file.read()
            print(text_to_write)

        with open(
            "classified_data.txt",
            "a",
        ) as file:
            file.write("\n" + text_to_write)

        print("Vault automatically sealed upon completion\n")
        print("All vault operations completed with maximum security.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found")


if __name__ == "__main__":
    ft_vault_security()
