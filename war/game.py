"""Game module"""

import logging
from enum import Enum
from random import shuffle
from typing import List, Tuple

from war.card import Card
from war.deck import Deck


class Game:
    """Game class"""

    def __init__(self) -> None:
        self._all_cards = self._create_cards()
        shuffle(self._all_cards)

        self._deck_a = Deck("A", self._all_cards[0::2])
        self._deck_b = Deck("B", self._all_cards[1::2])

        self._result = Game.Result.NOT_FINISHED
        self._number_of_turns = 0

    @staticmethod
    def _create_cards() -> List[Card]:
        cards = []
        for color in Card.Color:
            for figure in Card.Figure:
                cards.append(Card(figure, color))
        return cards

    def get_decks(self) -> Tuple[Deck, Deck]:
        """Returns created decks."""
        return self._deck_a, self._deck_b

    def _perform_turn_if_a_wins(self) -> bool:
        card_a = self._deck_a.take_next_card()
        card_b = self._deck_b.take_next_card()

        if card_a > card_b:
            self._deck_a.add_cards([card_a, card_b])
            return True
        if card_a < card_b:
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

    class Result(Enum):
        """Battle results."""
        A_WON, B_WON, TIMEOUT, NOT_FINISHED = range(4)

    TIMEOUT_TURN_THRESHOLD = 10000

    def perform_game(self) -> Tuple[Result, int]:
        """Performs game and returns number of turns."""
        while True:
            self._number_of_turns += 1
            logging.debug("Starting turn %s A=%s B=%s", self._number_of_turns,
                          self._deck_a.get_cards_number(), self._deck_b.get_cards_number())
            self._debug_stalled_games()
            if self._number_of_turns == Game.TIMEOUT_TURN_THRESHOLD:
                break
            try:
                self._perform_turn_if_a_wins()
            except IndexError:
                break

        return self._gather_results()

    def _debug_stalled_games(self) -> None:
        pass
        # if self._number_of_turns > Game.TIMEOUT_TURN_THRESHOLD - 10:
        #     print(self._deck_a)
        #     print(self._deck_b)

    def _gather_results(self) -> Tuple[Result, int]:
        print("Finished with {} A={} B={}".format(self._number_of_turns,
                                                  self._deck_a.get_cards_number(),
                                                  self._deck_b.get_cards_number()))
        # print(self._deck_a)
        # print(self._deck_b)
        if self._number_of_turns == Game.TIMEOUT_TURN_THRESHOLD:
            self._result = Game.Result.TIMEOUT
            return self._result, self._number_of_turns

        if self._deck_a.get_cards_number() == 0:
            self._result = Game.Result.A_WON
        elif self._deck_b.get_cards_number() == 0:
            self._result = Game.Result.B_WON
        else:
            assert False
        return self._result, self._number_of_turns
