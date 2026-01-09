from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict[str, str]:
        return self.__dict__ | {
            'type': self.__class__.__name__.split("Card")[0]
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
