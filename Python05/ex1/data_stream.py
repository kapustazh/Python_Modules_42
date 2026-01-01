#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        print(f"Initializing {self.__class__.__name__}...")
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Abstract method to process data."""
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter: returns data containing the criteria string."""
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in item]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        return {
            "stream_id": self.stream_id,
            "processed_items": self.processed_count,
            "type": self.__class__.__name__,
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Stream ID: {self.stream_id}, Type: Environmental Data")
        return ""


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        return ""


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        return ""


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams += [stream]


def data_stream_py() -> None:
    try:
        print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
        print()
        sensor1_id = "TEST"
        SensorStream(stream_id=sensor1_id).process_batch([])

    except Exception as e:
        print(f"Something went wrong -> {e}")


if __name__ == "__main__":
    data_stream_py()

# Authorized: class, def, super(), isinstance(), print(), try/except, list
# comprehensions,
