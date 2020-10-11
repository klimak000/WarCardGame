"""Single card module"""

import logging
from enum import Enum


class Card:
    """Single card class"""

    class Color(Enum):
        """Colors enum class."""
        Spades = 1  # pik / wino
        Hearts = 2  # serce / czeriweń
        Clubs = 3  # trefl / zołądź
        Diamonds = 4  # karo / dzwonek

    class Figure(Enum):
        """Figures enum class."""
        fig8, fig9, fig10, Jack, Queen, King, As = range(7)

    FigureToStrength = {
        Figure.fig8: 8,
        Figure.fig9: 9,
        Figure.fig10: 10,
        Figure.Jack: 11,
        Figure.Queen: 12,
        Figure.King: 13,
        Figure.As: 14
    }  # type Dict[Figure, int]

    def __init__(self, figure: Figure, color: Color) -> None:
        self._figure = figure
        self._color = color

        assert figure in Card.FigureToStrength.keys()
        self._strength = Card.FigureToStrength[figure]

        self._id = figure.value + 100 * color.value
        logging.debug("Created %s", self)

    def __str__(self):
        return("Card: id:{:2} strength:{:2} {:20} {}".
               format(self._id, self._strength, repr(self._color), repr(self._figure)))

    def __eq__(self, other):
        assert isinstance(other, self.__class__)
        return self._id == other.get_id()

    def __lt__(self, other):
        assert isinstance(other, self.__class__)
        return self._strength < other.get_strength()

    def __gt__(self, other):
        assert isinstance(other, self.__class__)
        return self._strength > other.get_strength()

    def get_strength(self) -> int:
        """Card strength."""
        return self._strength

    def get_id(self):
        """Card unique id."""
        return self._id
