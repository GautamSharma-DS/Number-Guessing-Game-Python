from dataclasses import dataclass
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
SCORES_FILE = DATA_DIR / "scores.json"
STATS_FILE = DATA_DIR / "stats.json"

STARTING_SCORE = 100
WRONG_GUESS_PENALTY = 10


@dataclass(frozen=True)
class Difficulty:
    name: str
    minimum: int
    maximum: int
    lives: int


DIFFICULTIES = {
    "1": Difficulty("Easy", 1, 20, 8),
    "2": Difficulty("Medium", 1, 50, 6),
    "3": Difficulty("Hard", 1, 100, 5),
}
