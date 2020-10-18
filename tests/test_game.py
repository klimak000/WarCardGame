"""File with Game class tests."""

from war.game import Game


def testing_creation_instance():
    game = Game()
    deck_a, deck_b = game.get_decks()
    assert deck_a.get_cards_number() == deck_b.get_cards_number()


def testing_performing_random_game():
    Game().perform_game()

# 38 - 55, 66 - 89
