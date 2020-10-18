#!/usr/bin/env python

""" Testing module."""

from war.game import Game


def _test2():
    unfinished = 0
    broken = 0
    a_wins = 0
    b_wins = 0
    numbers = []

    for _ in range(1000):
        game = Game()
        result, number = game.perform_game()

        if result == Game.Result.TIMEOUT:
            unfinished += 1
            continue
        if result == Game.Result.NOT_FINISHED:
            broken += 1
            continue

        if result == Game.Result.A_WON:
            a_wins += 1
        elif result == Game.Result.B_WON:
            b_wins += 1
        else:
            assert False
        numbers.append(number)

    numbers.sort()
    print(numbers)
    print("{} / {} = {}".format(sum(numbers), len(numbers),
                                sum(numbers) / len(numbers)))
    print("min {} max {}".format(min(numbers), max(numbers)))
    print("A:{} B:{} TO:{} B:{}".format(a_wins, b_wins, unfinished, broken))


def main():
    """The application's main entry point."""
    _test2()


if __name__ == "__main__":
    main()
