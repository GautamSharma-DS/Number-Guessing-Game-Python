import tempfile
import unittest
from pathlib import Path

from src.score_manager import ScoreManager


class TestScoreManager(unittest.TestCase):
    def test_score_manager_records_win(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            manager = ScoreManager(temp_path / "scores.json", temp_path / "stats.json")

            manager.record_game(
                won=True,
                score=80,
                guesses=3,
                difficulty="Hard",
                secret_number=73,
                player_name="Gautam",
            )

            stats = manager.get_statistics()
            self.assertEqual(stats["games_played"], 1)
            self.assertEqual(stats["games_won"], 1)
            self.assertEqual(stats["games_lost"], 0)
            self.assertEqual(stats["best_score"], 80)
            self.assertEqual(stats["average_guesses"], 3)
            self.assertEqual(manager.scores[0]["score"], 80)
            self.assertEqual(manager.scores[0]["player_name"], "Gautam")
            self.assertEqual(manager.get_leaderboard()[0]["score"], 80)

    def test_score_manager_records_loss(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            manager = ScoreManager(temp_path / "scores.json", temp_path / "stats.json")

            manager.record_game(
                won=False,
                score=0,
                guesses=5,
                difficulty="Hard",
                secret_number=73,
            )

            stats = manager.get_statistics()
            self.assertEqual(stats["games_played"], 1)
            self.assertEqual(stats["games_won"], 0)
            self.assertEqual(stats["games_lost"], 1)
            self.assertEqual(stats["best_score"], 0)

    def test_score_manager_can_reset_data(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            manager = ScoreManager(temp_path / "scores.json", temp_path / "stats.json")

            manager.record_game(
                won=True,
                score=90,
                guesses=2,
                difficulty="Easy",
                secret_number=12,
                player_name="Gautam",
            )
            manager.reset()

            stats = manager.get_statistics()
            self.assertEqual(stats["games_played"], 0)
            self.assertEqual(stats["best_score"], 0)
            self.assertEqual(manager.get_leaderboard(), [])


if __name__ == "__main__":
    unittest.main()
