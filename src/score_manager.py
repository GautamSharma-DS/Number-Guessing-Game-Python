import json
from datetime import datetime

try:
    from .config import SCORES_FILE, STATS_FILE
except ImportError:
    from config import SCORES_FILE, STATS_FILE


DEFAULT_STATS = {
    "games_played": 0,
    "games_won": 0,
    "games_lost": 0,
    "best_score": 0,
    "total_guesses": 0,
}


class ScoreManager:
    def __init__(self, scores_file=SCORES_FILE, stats_file=STATS_FILE):
        self.scores_file = scores_file
        self.stats_file = stats_file
        self.scores_file.parent.mkdir(parents=True, exist_ok=True)
        self.stats_file.parent.mkdir(parents=True, exist_ok=True)
        self.scores = self._load_json(self.scores_file, [])
        self.stats = self._load_json(self.stats_file, DEFAULT_STATS.copy())
        self._ensure_stats_shape()

    def _load_json(self, path, default):
        if not path.exists():
            self._save_json(path, default)
            return default

        try:
            with path.open("r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            self._save_json(path, default)
            return default

    def _save_json(self, path, data):
        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

    def _ensure_stats_shape(self):
        for key, value in DEFAULT_STATS.items():
            self.stats.setdefault(key, value)

    def record_game(
        self,
        won,
        score,
        guesses,
        difficulty,
        secret_number,
        player_name="Player",
    ):
        self.stats["games_played"] += 1
        self.stats["total_guesses"] += guesses

        if won:
            self.stats["games_won"] += 1
            self.stats["best_score"] = max(self.stats["best_score"], score)
            self.scores.append(
                {
                    "score": score,
                    "player_name": player_name,
                    "guesses": guesses,
                    "difficulty": difficulty,
                    "secret_number": secret_number,
                    "played_at": datetime.now().isoformat(timespec="seconds"),
                }
            )
            self.scores.sort(key=lambda item: item["score"], reverse=True)
            self.scores = self.scores[:10]
            self._save_json(self.scores_file, self.scores)
        else:
            self.stats["games_lost"] += 1

        self._save_json(self.stats_file, self.stats)

    def get_best_score(self):
        return self.stats.get("best_score", 0)

    def get_leaderboard(self):
        return self.scores

    def reset(self):
        self.scores = []
        self.stats = DEFAULT_STATS.copy()
        self._save_json(self.scores_file, self.scores)
        self._save_json(self.stats_file, self.stats)

    def get_statistics(self):
        games_played = self.stats["games_played"]
        games_won = self.stats["games_won"]
        win_rate = round((games_won / games_played) * 100, 2) if games_played else 0
        average_guesses = (
            round(self.stats["total_guesses"] / games_played, 2) if games_played else 0
        )

        return {
            "games_played": games_played,
            "games_won": games_won,
            "games_lost": self.stats["games_lost"],
            "win_rate": win_rate,
            "best_score": self.stats["best_score"],
            "average_guesses": average_guesses,
        }
