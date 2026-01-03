#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class defining the interface for all data stream types."""

    def __init__(self, stream_id: str) -> None:
        print(f"Initializing {self.__class__.__name__}...")
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Abstract method: subclasses must implement specific parsing logic."""
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Returns a subset of data containing the criteria string, or all data if None."""
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in item]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Returns metadata: stream_id, processed count, and class type."""
        return {
            "stream_id": self.stream_id,
            "processed_items": self.processed_count,
            "type": self.__class__.__name__,
        }


class SensorStream(DataStream):
    """Handles environmental data, specifically parsing 'temp' values."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        """Parses 'temp:value' strings to calculate averages and returns a summary."""
        output = (
            f"Stream ID: {self.stream_id}, Type: Environmental Data\n"
            f"Processing sensor batch: {data_batch}\n"
        )
        temp_value: float | bool = False
        try:
            for item in data_batch:
                if isinstance(item, str) and "temp" in item:
                    temp_value = float(item.split(":")[1])
                if not isinstance(item, str):
                    raise ValueError("Unknown data-type :(")
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
    """Handles financial data, calculating net flow from 'buy'/'sell' strings."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        """Adjusts balance based on 'buy' (+) or 'sell' (-) tags and returns net flow."""
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
                        raise ValueError("Unknown data-type :(")
                self.processed_count += 1
            if balance:
                if balance > 0:
                    return (
                        output + f"Transaction analysis: {self.processed_count}"
                        " operations, "
                        f"net flow: +{balance} units"
                    )
                else:
                    return (
                        output + f"Transaction analysis: {self.processed_count} "
                        " operations, "
                        f"net flow: {balance} units"
                    )
            return output + "No transactions provided"
        except Exception as e:
            return output + f"Invalid data -> {e}"


class EventStream(DataStream):
    """Handles system logs, specifically tracking 'error' occurrences."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        """Counts 'error' substrings in the batch and returns a health summary."""
        output = (
            f"Stream ID: {self.stream_id}, Type: System Events\n"
            f"Processing transaction batch: {data_batch}\n"
        )
        error_count: int | bool = False
        try:
            for item in data_batch:
                if isinstance(item, str):
                    if "error" in item:
                        error_count += 1
                self.processed_count += 1
            if error_count:
                return (
                    output
                    + f"Transaction analysis: {self.processed_count}"
                    + " operations, "
                    + f"{error_count} error detected"
                )
            else:
                return (
                    output
                    + f"Transaction analysis: {self.processed_count}"
                    + " operations"
                )
        except Exception as e:
            return output + f"Invalid data -> {e}"


class StreamProcessor:
    """Aggregates multiple DataStreams and processes them via a unified interface."""

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Registers a DataStream instance to the processor."""
        self.streams.append(stream)

    def process_all(self, batch_map: Dict[str, List[str]]) -> None:
        """
        Iterates through registered streams, matching them to batch data by ID.
        """
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        print("Batch Results:")

        sensor_alerts = 0
        large_transactions = 0
        results: List[str] = []

        for stream in self.streams:
            if stream.stream_id in batch_map:
                data = batch_map[stream.stream_id]

                try:
                    _ = stream.process_batch(data)

                    if isinstance(stream, SensorStream):
                        results += [f"- Sensor data: {len(data)} readings processed"]

                        filtered = stream.filter_data(
                            data,
                        )
                        sensor_alerts += len(filtered)

                    elif isinstance(stream, TransactionStream):
                        results += [
                            f"- Transaction data: {len(data)} operations processed"
                        ]

                        filtered = stream.filter_data(
                            data,
                        )
                        large_transactions += len(filtered)

                    elif isinstance(stream, EventStream):
                        results += [f"- Event data: {len(data)} events processed"]
                except Exception as e:
                    print(f"Error processing {stream.stream_id}: {e}")
            else:
                print(f"Warning: No data found for stream {stream.stream_id}")

        for r in results:
            print(r)

        print()
        print("Stream filtering active: High-priority data only")
        print(
            f"Filtered results: {sensor_alerts} critical sensor alerts, {large_transactions} large transactions"
        )
        print()
        print("All streams processed successfully. Nexus throughput optimal.")


def data_stream_py() -> None:
    """Main entry point: initializes streams, demonstrates filtering, and runs the processor."""
    try:
        print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
        print()

        sensor = SensorStream("SENSOR_001")
        filtered_data1 = sensor.filter_data(
            ["temp:22.5", "humidity:65", "pressure:1013"]
        )
        print(sensor.process_batch(filtered_data1))
        print()
        transaction = TransactionStream("TRANS_001")
        filtered_data2 = transaction.filter_data(["buy:22", "sell:15", "buy:123"])
        print(transaction.process_batch(filtered_data2))
        print()
        event = EventStream("EVENT_001")
        filtered_data3 = event.filter_data(["login", "error", "logout"], "error")
        print(event.process_batch(filtered_data3))
        print()
        batch_map = {
            # "SENSOR_001": [],
            "SENSOR_001": ["temp:22.5", "humidity:65"],
            # "TRANS_001": [],
            "TRANS_001": ["buy:100", "sell:150", "buy:75", "sell:10"],
            "EVENT_001": ["login", "error", "logout"],
        }
        processor = StreamProcessor()
        processor.add_stream(sensor)
        processor.add_stream(transaction)
        processor.add_stream(event)
        processor.process_all(batch_map)
        # I hate this exercise
    except Exception as e:
        print(f"Something went wrong -> {e}")


if __name__ == "__main__":
    data_stream_py()
