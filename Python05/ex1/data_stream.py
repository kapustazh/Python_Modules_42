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
        output = (
            f"Stream ID: {self.stream_id}, Type: Environmental Data\n"
            f"Processing sensor batch: {data_batch}\n"
        )
        temp_value: float | bool = False
        try:
            for item in data_batch:
                if isinstance(item, str) and "temp" in item:
                    temp_value = float(item.split(":")[1])
                if isinstance(item, str) is False:
                    raise ValueError("Uknown data-type :(")
                self.processed_count += 1
            if temp_value:
                return (
                    output + f"Sensor analysis: {self.processed_count} "
                    f"readings processed, avg temp: {temp_value}°C"
                )
            else:
                return (
                    output
                    + f"Sensor analysis: {self.processed_count}"
                    + " readings processed"
                )
        except Exception as e:
            return output + f"Invalid data -> {e}"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        output = (
            f"Stream ID: {self.stream_id}, Type: Financial Data\n"
            f"Processing transaction batch: {data_batch}\n"
        )
        balance: int | bool = False
        try:
            for item in data_batch:
                if isinstance(item, str):
                    if "buy" in item:
                        balance += int(item.split(":")[1])
                    elif "sell" in item:
                        balance -= int(item.split(":")[1])
                    else:
                        raise ValueError("Uknown data-type :(")
                self.processed_count += 1
            if balance:
                if balance > 0:
                    return (
                        output
                        + f"Transaction analysis: {self.processed_count}"
                        " operations, "
                        f"net flow: +{balance} units"
                    )
                else:
                    return (
                        output
                        + f"Transaction analysis: {self.processed_count} "
                        " operations, "
                        f"net flow: {balance} units"
                    )
            return output + "No transactions provided"
        except Exception as e:
            return output + f"Invalid data -> {e}"


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
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()
    sensor = SensorStream("FOO")
    filtered_data1 = sensor.filter_data(
        ["temp:22.5", "humidity:65", "pressure:1013"]
    )
    print(sensor.process_batch(filtered_data1))
    print()
    transaction = TransactionStream("BAR")
    filtered_data2 = transaction.filter_data(
        ["buy:22", "sell:15", "buy:123"]
    )
    print(transaction.process_batch(filtered_data2))


if __name__ == "__main__":
    data_stream_py()

# Authorized: class, def, super(), isinstance(), print(), try/except, list
# comprehensions,
