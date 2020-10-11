"""File with Card class tests."""

from war.card import Card


def testing_creation_instance():
    Card(Card.Figure.As, Card.Color.Hearts)


def testing_generating_id():
    tested = Card(Card.Figure.As, Card.Color.Hearts).get_id()
    expected = Card.Figure.As.value + 100 * Card.Color.Hearts.value
    assert tested == expected


def testing_reading_strength():
    tested = Card(Card.Figure.As, Card.Color.Hearts).get_strength()
    assert tested == Card.FigureToStrength[Card.Figure.As]


def testing_comparing_cards_strength():
    queen = Card(Card.Figure.Queen, Card.Color.Hearts)
    king = Card(Card.Figure.King, Card.Color.Hearts)
    assert queen < king
    assert king > queen
    assert not queen > king  # pylint: disable=C0113
    assert not king < queen  # pylint: disable=C0113
