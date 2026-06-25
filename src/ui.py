from time import sleep


def clear_screen():
    print("\n" * 2)


def line(char="=", width=44):
    print(char * width)


def welcome_screen():
    line()
    print("        NUMBER GUESSING GAME")
    line()


def show_menu():
    print("\n1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. View Statistics")
    print("5. View Leaderboard")
    print("6. Reset Scores")
    print("7. Exit")


def show_difficulty_info(difficulty):
    print(f"\n{difficulty.name}")
    print(f"Range : {difficulty.minimum} - {difficulty.maximum}")
    print(f"Lives : {difficulty.lives}")


def show_game_status(lives, guess_no, score, history, elapsed_seconds):
    line("=")
    print(f"Lives Left : {lives}")
    print(f"Guess No.  : {guess_no}")
    print(f"Score      : {score}")
    print(f"Timer      : {elapsed_seconds:.1f}s")
    if history:
        print(f"Previous   : {', '.join(str(guess) for guess in history)}")
    line("=")


def ask_choice(prompt):
    return input(prompt).strip()


def ask_int(prompt):
    value = input(prompt).strip()
    try:
        return int(value)
    except ValueError:
        return None


def show_hint(hint):
    icons = {
        "Very Close!": "🔥",
        "Much Lower": "📉",
        "Much Higher": "📈",
        "Too Low": "⬇️",
        "Too High": "⬆️",
        "Correct!": "✅",
    }
    print(f"{icons.get(hint, '💡')} {hint}")


def show_win_screen(player_name, secret_number, attempts, score, difficulty, elapsed_seconds):
    line()
    print("        YOU WIN")
    print(f"Player         : {player_name}")
    print(f"Correct Number : {secret_number}")
    print(f"Attempts       : {attempts}")
    print(f"Score          : {score}")
    print(f"Difficulty     : {difficulty}")
    print(f"Time           : {elapsed_seconds:.1f}s")
    line()


def show_lose_screen(secret_number):
    line()
    print("        GAME OVER")
    print(f"Correct Answer : {secret_number}")
    print("Better Luck Next Time")
    line()


def show_statistics(stats):
    line()
    print("        STATISTICS")
    print(f"Games Played    : {stats['games_played']}")
    print(f"Games Won       : {stats['games_won']}")
    print(f"Games Lost      : {stats['games_lost']}")
    print(f"Win Rate        : {stats['win_rate']}%")
    print(f"Best Score      : {stats['best_score']}")
    print(f"Average Guesses : {stats['average_guesses']}")
    line()


def show_leaderboard(scores):
    line()
    print("        LEADERBOARD")
    if not scores:
        print("No winning scores yet.")
    else:
        for index, score in enumerate(scores, start=1):
            player_name = score.get("player_name", "Player")
            print(
                f"{index}. {player_name} | {score['score']} pts | "
                f"{score['difficulty']} | {score['guesses']} guesses"
            )
    line()


def pause(message="\nPress Enter to continue..."):
    input(message)


def small_delay():
    sleep(0.25)
