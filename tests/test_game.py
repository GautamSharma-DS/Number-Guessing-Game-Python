import unittest

from src.config import DIFFICULTIES, STARTING_SCORE, WRONG_GUESS_PENALTY
from src.utils import calculate_score, get_hint, render_lives


class TestGameHelpers(unittest.TestCase):
    def test_difficulty_settings(self):
        self.assertEqual(DIFFICULTIES["1"].name, "Easy")
        self.assertEqual(DIFFICULTIES["1"].maximum, 20)
        self.assertEqual(DIFFICULTIES["3"].lives, 5)

    def test_score_decreases_for_wrong_guesses(self):
        self.assertEqual(
            calculate_score(0, STARTING_SCORE, WRONG_GUESS_PENALTY),
            100,
        )
        self.assertEqual(
            calculate_score(2, STARTING_SCORE, WRONG_GUESS_PENALTY),
            80,
        )
        self.assertEqual(
            calculate_score(20, STARTING_SCORE, WRONG_GUESS_PENALTY),
            0,
        )

    def test_hint_messages(self):
        self.assertEqual(get_hint(75, 73), "Very Close!")
        self.assertEqual(get_hint(75, 40), "Much Lower")
        self.assertEqual(get_hint(75, 95), "Much Higher")
        self.assertEqual(get_hint(75, 70), "Too Low")
        self.assertEqual(get_hint(75, 80), "Too High")

    def test_life_display(self):
        self.assertEqual(render_lives(3, 5), "♥♥♥♡♡")


if __name__ == "__main__":
    unittest.main()
