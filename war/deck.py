"""Single deck module"""

from typing import List

from war.card import Card


class Deck:
    """Single deck class"""

    def __init__(self, name: str) -> None:
        self._name = name
        self._cards = []  # type: List[Card]

    def __str__(self):
        print("Deck {} number of cards {}".
              format(self._name, self.get_card_number()))
        for card in self._cards:
            print(card)
        print("-")
        return ""

    def add_cards(self, cards: List[Card]):
        """Add cards to deck."""
        for card in cards:
            self._cards.append(card)

    def _remove_card(self, card: Card):
        """Remove card from deck."""
        self._cards.remove(card)

    def take_next_card(self) -> Card:
        """Take (remove and get) card from deck."""
        card = self._cards[0]
        self._remove_card(card)
        return card

    def get_card_number(self) -> int:
        """Card unique id."""
        return len(self._cards)
