import sys


def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    print("Input Stream active. Enter archivist ID:", end=" ")
    archivist_id = input()

    print("Input Stream active. Enter status report:", end=" ")
    status_report = input()

    print()

    print(
        f"[STANDARD] Archive status from {archivist_id}: {status_report}",
        file=sys.stdout,
    )

    output_string = "[ALERT] System diagnostic:"
    print(output_string, "Communication channels verified", file=sys.stderr)

    print("[STANDARD] Data transmission complete", file=sys.stdout)

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    ft_stream_management()
