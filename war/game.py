"""Game module"""

from random import shuffle
from typing import List, Optional

from war.card import Card
from war.deck import Deck


class Game:
    """Game class"""

    def __init__(self) -> None:
        self._deck_a = Deck("A")
        self._deck_b = Deck("B")

        self._cards = self._create_cards()
        self._shuffle_cards()
        self._deck_a.add_cards(self._cards[0::2])
        self._deck_b.add_cards(self._cards[1::2])

        self._number_of_turns = 0
        self._a_won = None  # type: Optional[bool]

    @staticmethod
    def _create_cards() -> List[Card]:
        cards = []
        for color in Card.Color:
            for figure in Card.Figure:
                cards.append(Card(figure, color))
        return cards

    def _shuffle_cards(self):
        # print(self._cards)
        shuffle(self._cards)
        # print(self._cards)

    # class TurnResult(Enum):
    #     A_WINS, B_WINS, DRAW = range(3)

    def _perform_turn_if_a_wins(self) -> bool:
        card_a = self._deck_a.take_next_card()
        card_b = self._deck_b.take_next_card()

        if card_a.get_strength() > card_b.get_strength():
            self._deck_a.add_cards([card_a, card_b])
            return True
        if card_a.get_strength() < card_b.get_strength():
            self._deck_b.add_cards([card_b, card_a])
            return False
        # it's draw!
        card_a_bis = self._deck_a.take_next_card()
        card_b_bis = self._deck_b.take_next_card()
        if self._perform_turn_if_a_wins():
            self._deck_a.add_cards([card_a_bis, card_b_bis, card_a, card_b])
            return True

        self._deck_b.add_cards([card_b_bis, card_a_bis, card_b, card_a])
        return False


    def perform_game(self) -> int:
        """Performs game and returns number of turns."""
        while True:
            self._number_of_turns += 1
            print("Starting turn {} A={} B={}".format(self._number_of_turns,
                                                      self._deck_a.get_card_number(),
                                                      self._deck_b.get_card_number()))
            try:
                self._perform_turn_if_a_wins()
            except IndexError:
                break
            # if self._number_of_turns > 59990:
            #     print(self._deck_a)
            #     print(self._deck_b)
            if self._number_of_turns == 10000:
                break
        # print(self._deck_a)
        # print(self._deck_b)
        print("Finished with {} A={} B={}".format(self._number_of_turns,
                                                  self._deck_a.get_card_number(),
                                                  self._deck_b.get_card_number()))
        if self._deck_a.get_card_number() == 0:
            self._a_won = False
        else:
            self._a_won = True
        return self._number_of_turns

    def get_if_a_won(self) -> bool:
        """Get info if A wins."""
        assert self._a_won is not None
        return self._a_won
