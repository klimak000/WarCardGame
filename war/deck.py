"""Single deck module"""

import logging
from typing import List

from war.card import Card


class Deck:
    """Single deck class"""

    def __init__(self, name: str, cards: List[Card]) -> None:
        self._name = name
        self._cards = cards  # type: List[Card]
        logging.debug("Created %s", self)

    def __str__(self):
        text = "Deck {}, number of cards is {}\n".format(self._name, self.get_cards_number())
        for card in self._cards:
            text += '{}\n'.format(card)
        return text

    def add_cards(self, cards: List[Card]):
        """Add (to end) cards to deck."""
        for card in cards:
            assert card not in self._cards
            self._cards.append(card)

    def take_next_card(self) -> Card:
        """Take (remove and get) first card from deck."""
        card = self._cards[0]
        self._cards.remove(card)
        return card

    def get_cards_number(self) -> int:
        """Returns number of cards in deck."""
        return len(self._cards)
