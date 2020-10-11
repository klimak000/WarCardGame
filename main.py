""" Testing module."""

import logging

from war.game import Game


def _test2():
    unfinished = 0
    a_wins = 0
    b_wins = 0
    numbers = []
    for _ in range(1000):
        game = Game()
        number = game.perform_game()
        if number == 10000:
            unfinished += 1
        else:
            numbers.append(number)
            if game.get_if_a_won():
                a_wins += 1
            else:
                b_wins += 1
    numbers.sort()
    print(numbers)
    print("{} / {} = {}".format(sum(numbers), len(numbers),
                                sum(numbers) / len(numbers)))
    print("min {} max {}".format(min(numbers), max(numbers)))
    print("A:{} B:{} U:{}".format(a_wins, b_wins, unfinished))


def main():
    # TODO TIME
    _test2()


if __name__ == "__main__":
    main()
