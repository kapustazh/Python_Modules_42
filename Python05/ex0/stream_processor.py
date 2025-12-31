#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Abstract base class acting as a blueprint for all processors."""

    def run(self, data: Any) -> None:
        """Template method that orchestrates the execution flow: initialize,
        validate, process, and print."""
        name = self.__class__.__name__
        print(f"Initializing {name}...")

        # Display input data with quotes if it is a string
        if isinstance(data, str):
            print(f'Processing data: "{data}"')
        else:
            print(f"Processing data: {data}")

        if self.validate(data):
            # Conditional logging based on the class name
            if "Numeric" in name:
                print("Validation: Numeric data verified")
            elif "Text" in name:
                print("Validation: Text data verified")
            elif "Log" in name:
                print("Validation: Log entry verified")

            output = self.process(data)
            print(self.format_output(output))

    @abstractmethod
    def process(self, data: Any) -> str:
        """Abstract method: Children must implement their own logic
        to process data."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Abstract method: Children must implement their own logic
        to check data validity."""
        pass

    def format_output(self, result: str) -> str:
        """Default formatting method, can be overridden by children."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Concrete class for handling lists of numbers."""

    def process(self, data: Any) -> str:
        """Calculates count, sum, and average of the number list."""
        return (
            f"Processed {len(data)} numeric values, "
            f"sum={sum(data)}, avg={sum(data) / len(data)}"
        )

    def validate(self, data: Any) -> bool:
        """Checks if data is iterable and contains numbers
        (using modulo to test numeric type)."""
        try:
            for _ in data:
                _ %= 1
            return True
        except Exception:
            print("Validation failed: Not numeric data!")

    def format_output(self, result: str) -> str:
        """Returns standard output format for numbers."""
        return f"Output: {result}"


class TextProcessor(DataProcessor):
    """Concrete class for handling string text."""

    def process(self, data: Any) -> str:
        """Counts total characters and words in the text."""
        return f"{len(data)} characters, {len(data.split())} words"

    def validate(self, data: Any) -> bool:
        """Checks if data is a string (slicable)."""
        try:
            data = data[::1]
            return True
        except Exception:
            print("Validation failed: Not text data!")
            return False

    def format_output(self, result: str) -> str:
        """Overrides format to add 'Processed text:' prefix."""
        return f"Output: Processed text: {result}"


class LogProcessor(DataProcessor):
    """Concrete class for parsing system log messages."""

    def process(self, data: Any) -> str:
        """Extracts messages based on log tags (ERROR, INFO, STATUS)."""
        if "ERROR:" in data:
            return f"[ALERT] ERROR level detected: {data[7::]}"
        elif "INFO:" in data:
            return f"[INFO] INFO level detected: {data[6::]}"
        elif "STATUS:" in data:
            return f"[STATUS]: {data[8::]}"

    def validate(self, data: Any) -> bool:
        """Ensures data contains valid log keywords (ERROR, STATUS, INFO)."""
        try:
            data = "" + data
            if "ERROR:" in data or "STATUS:" in data or "INFO:" in data:
                return True
            else:
                raise ValueError
        except Exception:
            print("Validation failed: Not log data!")
            return False

    def format_output(self, result: str) -> str:
        """Returns standard output format for logs."""
        return f"Output: {result}"


def stream_processor() -> None:
    """Main execution function to demonstrate both verbose
    and polymorphic usage."""
    try:
        print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
        print()
        numeric = NumericProcessor()
        numeric.run([1, 2, 3, 4, 5])
        print()
        text = TextProcessor()
        text.run("Hello Nexus World")
        print()
        log = LogProcessor()
        log.run("ERROR: Connection timeout")
        print()

        print("=== Polymorphic Processing Demo ===")
        print("Processing multiple data types through same interface...")
        tasks = [
            (NumericProcessor(), [1, 2, 3]),
            (TextProcessor(), "Hello World!"),
            (LogProcessor(), "INFO: System ready"),
        ]
        count = 1
        for my_processor, data in tasks:
            if my_processor.validate(data):
                result = my_processor.process(data)
                print(f"Result {count}: {result}")
                count += 1
        print()
        print("Foundation systems online. Nexus ready for advanced streams.")
    except Exception as e:
        print(f"Something went wrong -> {e}")


if __name__ == "__main__":
    stream_processor()
