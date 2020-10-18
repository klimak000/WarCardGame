"""File with Game class tests."""

from unittest.mock import patch

from war.card import Card
from war.deck import Deck
from war.game import Game


def testing_creation_instance():
    game = Game()
    deck_a, deck_b = game.get_decks()
    assert deck_a.get_cards_number() == deck_b.get_cards_number()


def testing_performing_random_game():
    Game().perform_game()


def testing_winning_game_by_both_players():
    def _get_winner() -> Deck:
        return Deck("Winner", [Card(Card.Figure.Queen, Card.Color.Hearts)])

    def _get_loser() -> Deck:
        return Deck("Loser", [Card(Card.Figure.King, Card.Color.Hearts)])

    game = Game()
    game.set_custom_decks(_get_winner(), _get_loser())
    result, turns = game.perform_game()
    assert result == Game.Result.A_WON
    assert turns == 2

    game = Game()
    game.set_custom_decks(_get_loser(), _get_winner())
    result, turns = game.perform_game()
    assert result == Game.Result.B_WON
    assert turns == 2


def testing_exiting_stalled_games():
    game = Game()
    with patch.object(Game, '_perform_duel', return_value=None):
        result, turns = game.perform_game()
        assert result == Game.Result.TIMEOUT
        assert turns == Game.TIMEOUT_TURN_THRESHOLD
