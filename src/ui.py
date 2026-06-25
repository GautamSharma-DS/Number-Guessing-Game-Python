from time import sleep


WIDTH = 50


def clear_screen():
    print("\n" * 2)


def line(char="=", width=WIDTH):
    print(char * width)


def title(text):
    line()
    print(text.center(WIDTH))
    line()


def section(text):
    print()
    line("-")
    print(text.center(WIDTH))
    line("-")


def row(label, value):
    print(f"{label:<16}: {value}")


def welcome_screen():
    title("NUMBER GUESSING GAME")


def show_menu():
    print()
    print("1. Easy              Range 1-20    Lives 8")
    print("2. Medium            Range 1-50    Lives 6")
    print("3. Hard              Range 1-100   Lives 5")
    print("4. View Statistics")
    print("5. View Leaderboard")
    print("6. Reset Scores")
    print("7. Exit")


def show_difficulty_info(difficulty):
    section("GAME SETUP")
    row("Difficulty", difficulty.name)
    row("Range", f"{difficulty.minimum} - {difficulty.maximum}")
    row("Lives", difficulty.lives)


def show_game_status(lives, guess_no, score, history, elapsed_seconds):
    line()
    row("Lives Left", lives)
    row("Guess No.", guess_no)
    row("Score", score)
    row("Timer", f"{elapsed_seconds:.1f}s")
    if history:
        row("Previous", ", ".join(str(guess) for guess in history))
    line()


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
        "Very Close!": "\U0001f525",
        "Much Lower": "\U0001f4c9",
        "Much Higher": "\U0001f4c8",
        "Too Low": "\u2b07\ufe0f",
        "Too High": "\u2b06\ufe0f",
        "Correct!": "\u2705",
    }
    default_icon = "\U0001f4a1"
    print(f"\n{icons.get(hint, default_icon)} {hint}\n")


def show_win_screen(player_name, secret_number, attempts, score, difficulty, elapsed_seconds):
    title("YOU WIN")
    row("Player", player_name)
    row("Correct Number", secret_number)
    row("Attempts", attempts)
    row("Score", score)
    row("Difficulty", difficulty)
    row("Time", f"{elapsed_seconds:.1f}s")
    line()


def show_lose_screen(secret_number):
    title("GAME OVER")
    row("Correct Answer", secret_number)
    print("Better Luck Next Time".center(WIDTH))
    line()


def show_statistics(stats):
    title("STATISTICS")
    row("Games Played", stats["games_played"])
    row("Games Won", stats["games_won"])
    row("Games Lost", stats["games_lost"])
    row("Win Rate", f"{stats['win_rate']}%")
    row("Best Score", stats["best_score"])
    row("Average Guesses", stats["average_guesses"])
    line()


def show_leaderboard(scores):
    title("LEADERBOARD")
    if not scores:
        print("No winning scores yet.".center(WIDTH))
    else:
        print(f"{'Rank':<6}{'Player':<14}{'Score':<8}{'Mode':<10}{'Guesses'}")
        line("-")
        for index, score in enumerate(scores, start=1):
            player_name = score.get("player_name", "Player")[:13]
            print(
                f"{index:<6}{player_name:<14}{score['score']:<8}"
                f"{score['difficulty']:<10}{score['guesses']}"
            )
    line()


def pause(message="\nPress Enter to continue..."):
    input(message)


def small_delay():
    sleep(0.25)
