"""File with Game class tests."""

from unittest.mock import patch

from war.card import Card
from war.deck import Deck
from war.game import Game


def testing_creation_instance() -> None:
    game = Game()
    deck_a, deck_b = game.get_decks()
    assert len(deck_a) == len(deck_b)


def testing_performing_random_game() -> None:
    Game().perform_game()


def _perform_short_game(deck_a: Deck, deck_b: Deck, winner: Game.Result) -> Game:
    game = Game()
    game.set_custom_decks(deck_a, deck_b)

    result, turns = game.perform_game()
    assert turns == 2
    assert result == winner
    return game


def testing_winning_game_by_both_players() -> None:
    def _get_winner() -> Deck:
        return Deck("Winner", [Card(Card.Figure.King, Card.Color.Hearts)])

    def _get_loser() -> Deck:
        return Deck("Loser", [Card(Card.Figure.Queen, Card.Color.Hearts)])

    _perform_short_game(_get_winner(), _get_loser(), Game.Result.A_WON)
    _perform_short_game(_get_loser(), _get_winner(), Game.Result.B_WON)


def testing_ordering_playoff_cards() -> None:
    card_winner_1 = Card(Card.Figure.Queen, Card.Color.Hearts)
    card_winner_2 = Card(Card.Figure.Jack, Card.Color.Hearts)
    card_winner_3 = Card(Card.Figure.fig10, Card.Color.Hearts)
    card_loser_1 = Card(Card.Figure.Queen, Card.Color.Spades)
    card_loser_2 = Card(Card.Figure.Jack, Card.Color.Spades)
    card_loser_3 = Card(Card.Figure.fig9, Card.Color.Spades)

    def _get_winner() -> Deck:
        return Deck("Winner", [card_winner_1, card_winner_2, card_winner_3])

    def _get_loser() -> Deck:
        return Deck("Loser", [card_loser_1, card_loser_2, card_loser_3])

    game = _perform_short_game(_get_winner(), _get_loser(), Game.Result.A_WON)
    deck_a, deck_b = game.get_decks()
    assert len(deck_a) == 5  # one card was taken to next duel
    assert len(deck_b) == 0
    assert deck_a.take_next_card() == card_loser_3
    assert deck_a.take_next_card() == card_winner_2
    assert deck_a.take_next_card() == card_loser_2
    assert deck_a.take_next_card() == card_winner_1
    assert deck_a.take_next_card() == card_loser_1

    game = _perform_short_game(_get_loser(), _get_winner(), Game.Result.B_WON)
    deck_a, deck_b = game.get_decks()
    assert len(deck_a) == 0
    assert len(deck_b) == 6
    assert deck_b.take_next_card() == card_winner_3
    assert deck_b.take_next_card() == card_loser_3
    assert deck_b.take_next_card() == card_winner_2
    assert deck_b.take_next_card() == card_loser_2
    assert deck_b.take_next_card() == card_winner_1
    assert deck_b.take_next_card() == card_loser_1


def testing_exiting_stalled_games() -> None:
    game = Game()
    with patch.object(Game, '_perform_duel', return_value=None):
        result, turns = game.perform_game()
        assert result == Game.Result.TIMEOUT
        assert turns == Game.TIMEOUT_TURN_THRESHOLD
