"""Single card module"""

from enum import Enum


class Card:
    """Single card class"""

    class Color(Enum):
        """Colors enum class."""
        Spades = 0  # pik / wino
        Hearts = 7  # serce / czeriweń
        Clubs = 14  # trefl / zołądź
        Diamonds = 21  # karo / dzwonek

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

        self._id = figure.value + color.value
        # print(self)

    def __str__(self):
        return("Card: id:{:2} strength:{:2} {:20} {}".
               format(self._id, self._strength, repr(self._color), repr(self._figure)))

    def get_strength(self) -> int:
        """Card strength."""
        return self._strength

    def get_id(self):
        """Card unique id."""
        return self._id
