#!/usr/bin/env python

"""Testing module."""

import logging
from argparse import ArgumentParser
from typing import List

from war.game import Game


class WarCardGameTest:
    """Testing class."""

    def __init__(self) -> None:
        self._tests_number = 0
        self.unfinished = 0
        self.broken = 0
        self.a_wins = 0
        self.b_wins = 0
        self.numbers = []  # type: List[int]
        self._average_turns_number = -1.0

        self._setup_argparse()

    def get_result(self) -> float:
        """Get main result of the test."""
        return self._average_turns_number

    def _setup_argparse(self) -> None:
        parser = ArgumentParser()
        parser.add_argument(
            "--log",
            default=logging.INFO,
            type=lambda x: getattr(logging, x),  # type: ignore
            help="Configure the logging level.")
        parser.add_argument(
            "--number",
            default=1000,
            type=int,
            help="Setup number of generated games.")

        args = parser.parse_args()
        logging.basicConfig(level=args.log)
        self._tests_number = args.number

    def _test(self) -> None:
        """Main test."""
        for _ in range(self._tests_number):
            game = Game()
            result, number = game.perform_game()

            if result == Game.Result.TIMEOUT:
                self.unfinished += 1
                continue
            if result == Game.Result.NOT_FINISHED:
                self.broken += 1
                continue

            if result == Game.Result.A_WON:
                self.a_wins += 1
            elif result == Game.Result.B_WON:
                self.b_wins += 1
            else:
                assert False
            self.numbers.append(number)

        self.numbers.sort()
        self._average_turns_number = sum(self.numbers) / len(self.numbers)

        logging.info(self.numbers)
        logging.info("%i / %i = %i", sum(self.numbers), len(self.numbers),
                     self._average_turns_number)
        logging.info("min %i max %i", min(self.numbers), max(self.numbers))
        logging.info("A:%i B:%i TO:%i B:%i", self.a_wins, self.b_wins, self.unfinished, self.broken)

    def main(self) -> None:
        """The application's main entry point."""
        self._test()


if __name__ == "__main__":
    WarCardGameTest().main()
