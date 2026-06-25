import random
from time import perf_counter

try:
    from .config import DIFFICULTIES, STARTING_SCORE, WRONG_GUESS_PENALTY
    from .player import Player
    from .score_manager import ScoreManager
    from .sound_manager import SoundManager
    from .ui import (
        ask_choice,
        ask_int,
        clear_screen,
        pause,
        show_difficulty_info,
        show_game_status,
        show_hint,
        show_leaderboard,
        show_lose_screen,
        show_menu,
        show_statistics,
        show_win_screen,
        small_delay,
        welcome_screen,
    )
    from .utils import calculate_score, get_hint, render_lives
except ImportError:
    from config import DIFFICULTIES, STARTING_SCORE, WRONG_GUESS_PENALTY
    from player import Player
    from score_manager import ScoreManager
    from sound_manager import SoundManager
    from ui import (
        ask_choice,
        ask_int,
        clear_screen,
        pause,
        show_difficulty_info,
        show_game_status,
        show_hint,
        show_leaderboard,
        show_lose_screen,
        show_menu,
        show_statistics,
        show_win_screen,
        small_delay,
        welcome_screen,
    )
    from utils import calculate_score, get_hint, render_lives


class NumberGuessingGame:
    def __init__(self, score_manager=None, sound_manager=None):
        self.score_manager = score_manager or ScoreManager()
        self.sound_manager = sound_manager or SoundManager()

    def run(self):
        while True:
            clear_screen()
            welcome_screen()
            print(f"Best Score : {self.score_manager.get_best_score()}")
            show_menu()
            choice = ask_choice("\nSelect Difficulty: ")

            if choice in DIFFICULTIES:
                self.play_round(DIFFICULTIES[choice])
            elif choice == "4":
                clear_screen()
                show_statistics(self.score_manager.get_statistics())
                pause()
            elif choice == "5":
                clear_screen()
                show_leaderboard(self.score_manager.get_leaderboard())
                pause()
            elif choice == "6":
                self.reset_scores()
            elif choice == "7":
                print("\nThanks for playing!")
                break
            else:
                print("\nInvalid choice. Please select 1 to 7.")
                small_delay()

    def reset_scores(self):
        confirm = ask_choice("Reset all scores and statistics? (y/n): ").lower()
        if confirm == "y":
            self.score_manager.reset()
            print("Scores and statistics reset.")
        else:
            print("Reset cancelled.")
        small_delay()

    def play_round(self, difficulty):
        while True:
            self._play_single_game(difficulty)
            print("\nPlay Again?")
            print("1. Yes")
            print("2. No")
            if ask_choice("Select: ") != "1":
                break

    def _play_single_game(self, difficulty):
        secret_number = random.randint(difficulty.minimum, difficulty.maximum)
        player_name = ask_choice("Enter Player Name: ") or "Player"
        player = Player(player_name)
        lives_left = difficulty.lives
        wrong_guesses = 0
        start_time = perf_counter()

        clear_screen()
        show_difficulty_info(difficulty)

        while lives_left > 0:
            score = calculate_score(
                wrong_guesses, STARTING_SCORE, WRONG_GUESS_PENALTY
            )
            lives_display = render_lives(lives_left, difficulty.lives)
            show_game_status(
                lives_display,
                len(player.guess_history) + 1,
                score,
                player.guess_history,
                perf_counter() - start_time,
            )

            guess = ask_int(
                f"Enter Guess ({difficulty.minimum}-{difficulty.maximum}): "
            )

            if guess is None:
                print("Please enter a valid number.")
                self.sound_manager.error()
                continue

            if guess < difficulty.minimum or guess > difficulty.maximum:
                print(
                    f"Guess must be between {difficulty.minimum} and {difficulty.maximum}."
                )
                self.sound_manager.error()
                continue

            player.add_guess(guess)

            if guess == secret_number:
                elapsed_seconds = perf_counter() - start_time
                final_score = calculate_score(
                    wrong_guesses, STARTING_SCORE, WRONG_GUESS_PENALTY
                )
                self.sound_manager.win()
                show_win_screen(
                    player.name,
                    secret_number,
                    len(player.guess_history),
                    final_score,
                    difficulty.name,
                    elapsed_seconds,
                )
                self.score_manager.record_game(
                    won=True,
                    score=final_score,
                    guesses=len(player.guess_history),
                    difficulty=difficulty.name,
                    secret_number=secret_number,
                    player_name=player.name,
                )
                return

            wrong_guesses += 1
            lives_left -= 1
            self.sound_manager.wrong()
            show_hint(get_hint(secret_number, guess))

        self.sound_manager.lose()
        show_lose_screen(secret_number)
        self.score_manager.record_game(
            won=False,
            score=0,
            guesses=len(player.guess_history),
            difficulty=difficulty.name,
            secret_number=secret_number,
            player_name=player.name,
        )
