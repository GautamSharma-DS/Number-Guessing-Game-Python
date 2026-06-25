try:
    from .game import NumberGuessingGame
except ImportError:
    from game import NumberGuessingGame


def main():
    game = NumberGuessingGame()
    game.run()


if __name__ == "__main__":
    main()
