from abc import ABC, abstractmethod


class Card(ABC):
    """Abstract base class of the Card"""
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Method to be implemented in inhertied class"""
        pass

    def get_card_info(self) -> dict:
        """Get's attributes of the class

        Returns:
            dict: union of te all attributes + type with name
        """
        return self.__dict__ | {
            'type': self.__class__.__name__.split("Card")[0]
        }

    def is_playable(self, available_mana: int) -> bool:
        """Method to check if we have enough mana
        to call this function
        Args:
            available_mana (int): mana from the main()

        Returns:
            bool: if card can be thrown
        """
        return available_mana >= self.cost
