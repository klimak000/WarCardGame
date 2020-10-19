"""Game module"""

import logging
from enum import Enum
from random import shuffle
from typing import List, Tuple

from war.card import Card
from war.deck import Deck


class Game:
    """Game class"""

    class Result(Enum):
        """Battle results."""
        A_WON, B_WON, TIMEOUT, NOT_FINISHED = range(4)

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

    def set_custom_decks(self, deck_a: Deck, deck_b: Deck) -> None:
        """Change created decks to custom decks."""
        self._deck_a = deck_a
        self._deck_b = deck_b

    def get_decks(self) -> Tuple[Deck, Deck]:
        """Returns created decks."""
        return self._deck_a, self._deck_b

    def _perform_duel(self) -> Result:
        """Perform single duel.

        Order of returning cards to deck has big importance.
        Read README for more information.
        Function puts back cards to deck in order:
            normal duel:
                1 winner card
                2 loser card
            duel with playoff:
                1 winner card from second duel
                2 loser card from second duel
                3 winner hidden card
                4 loser hidden card
                5 winner card from first duel
                6 loser card from first duel

        Returns:
            Result: A_WON if player a won, B_WON otherwise.
        """
        card_a = self._deck_a.take_next_card()
        card_b = self._deck_b.take_next_card()

        if card_a > card_b:
            self._deck_a.add_cards([card_a, card_b])
            return Game.Result.A_WON
        if card_a < card_b:
            self._deck_b.add_cards([card_b, card_a])
            return Game.Result.B_WON

        # it's draw!
        card_a_hidden = self._deck_a.take_next_card()
        card_b_hidden = self._deck_b.take_next_card()
        play_off = self._perform_duel()
        assert play_off in (Game.Result.A_WON, Game.Result.B_WON)

        if play_off == Game.Result.A_WON:
            self._deck_a.add_cards([card_a_hidden, card_b_hidden, card_a, card_b])
            return Game.Result.A_WON
        self._deck_b.add_cards([card_b_hidden, card_a_hidden, card_b, card_a])
        return Game.Result.B_WON

    def _perform_turn(self) -> bool:
        """Perform single turn.
        Returns:
            bool: False if game is finished, True otherwise.
        """
        self._number_of_turns += 1
        logging.debug("Starting turn %s A=%s B=%s", self._number_of_turns,
                      len(self._deck_a), len(self._deck_b))
        try:
            self._perform_duel()
        except IndexError:  # one of deck is out of cards, game is finished
            return False
        return True

    TIMEOUT_TURN_THRESHOLD = 10000

    def perform_game(self) -> Tuple[Result, int]:
        """Performs game and returns number of turns."""
        while self._perform_turn():
            if self._debug_against_stalled_games():
                break
        return self._gather_results()

    def _debug_against_stalled_games(self) -> bool:
        if self._number_of_turns > Game.TIMEOUT_TURN_THRESHOLD - 10:
            logging.debug(self._deck_a)
            logging.debug(self._deck_b)
        if self._number_of_turns == Game.TIMEOUT_TURN_THRESHOLD:
            self._result = Game.Result.TIMEOUT
            return True
        return False

    def _gather_results(self) -> Tuple[Result, int]:
        logging.info("Finished with %d A=%d B=%d", self._number_of_turns,
                     len(self._deck_a), len(self._deck_b))
        if self._result == Game.Result.TIMEOUT:
            return self._result, self._number_of_turns

        a_number = len(self._deck_a)
        b_number = len(self._deck_b)

        if a_number == 0:
            assert b_number != 0
            self._result = Game.Result.B_WON
            return self._result, self._number_of_turns

        assert a_number != 0 and b_number == 0
        self._result = Game.Result.A_WON
        return self._result, self._number_of_turns
