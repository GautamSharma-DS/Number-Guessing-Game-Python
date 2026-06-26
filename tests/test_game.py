from src.config import DIFFICULTIES, STARTING_SCORE, WRONG_GUESS_PENALTY
from src.utils import calculate_score, get_hint, render_lives


def test_difficulty_settings():
    assert DIFFICULTIES["1"].name == "Easy"
    assert DIFFICULTIES["1"].maximum == 20
    assert DIFFICULTIES["3"].lives == 5


def test_score_decreases_for_wrong_guesses():
    assert calculate_score(0, STARTING_SCORE, WRONG_GUESS_PENALTY) == 100
    assert calculate_score(2, STARTING_SCORE, WRONG_GUESS_PENALTY) == 80
    assert calculate_score(20, STARTING_SCORE, WRONG_GUESS_PENALTY) == 0


def test_hint_messages():
    assert get_hint(75, 73) == "Very Close!"
    assert get_hint(75, 40) == "Much Lower"
    assert get_hint(75, 95) == "Much Higher"
    assert get_hint(75, 70) == "Too Low"
    assert get_hint(75, 80) == "Too High"


def test_life_display():
    assert render_lives(3, 5) == "\u2665\u2665\u2665\u2661\u2661"
