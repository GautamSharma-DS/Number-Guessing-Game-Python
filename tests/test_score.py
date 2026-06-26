from src.score_manager import ScoreManager


def test_score_manager_records_win(tmp_path):
    manager = ScoreManager(tmp_path / "scores.json", tmp_path / "stats.json")

    manager.record_game(
        won=True,
        score=80,
        guesses=3,
        difficulty="Hard",
        secret_number=73,
        player_name="Gautam",
    )

    stats = manager.get_statistics()
    assert stats["games_played"] == 1
    assert stats["games_won"] == 1
    assert stats["games_lost"] == 0
    assert stats["best_score"] == 80
    assert stats["average_guesses"] == 3
    assert manager.scores[0]["score"] == 80
    assert manager.scores[0]["player_name"] == "Gautam"
    assert manager.get_leaderboard()[0]["score"] == 80


def test_score_manager_records_loss(tmp_path):
    manager = ScoreManager(tmp_path / "scores.json", tmp_path / "stats.json")

    manager.record_game(
        won=False,
        score=0,
        guesses=5,
        difficulty="Hard",
        secret_number=73,
    )

    stats = manager.get_statistics()
    assert stats["games_played"] == 1
    assert stats["games_won"] == 0
    assert stats["games_lost"] == 1
    assert stats["best_score"] == 0


def test_score_manager_can_reset_data(tmp_path):
    manager = ScoreManager(tmp_path / "scores.json", tmp_path / "stats.json")

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
    assert stats["games_played"] == 0
    assert stats["best_score"] == 0
    assert manager.get_leaderboard() == []
