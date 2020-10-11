"""File with Deck class tests."""

import pytest

from war.card import Card
from war.deck import Deck


def _get_card_example():
    return Card(Card.Figure.As, Card.Color.Hearts)


def _create_instance():
    return Deck("ABC", [_get_card_example()])


def test_creation_instance():
    deck = _create_instance()
    assert deck.take_next_card().get_id() == _get_card_example().get_id()


def test_adding_card():
    deck = _create_instance()
    assert deck.get_cards_number() == 1
    deck.add_cards([Card(Card.Figure.As, Card.Color.Clubs)])
    assert deck.get_cards_number() == 2


def test_against_adding_existing_card():
    deck = _create_instance()
    assert deck.get_cards_number() == 1
    with pytest.raises(AssertionError):
        deck.add_cards([_get_card_example()])
