from abc import ABC, abstractmethod


class Combatable(ABC):

    @abstractmethod
    def attack(self, target) -> dict:
        ...

    def defend(self, incoming_damage: int) -> dict:
        ...

    def get_combat_stats(self) -> dict:
        ...
