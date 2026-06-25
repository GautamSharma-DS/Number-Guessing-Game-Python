def clamp_score(score):
    return max(0, score)


def calculate_score(wrong_guesses, starting_score, penalty):
    return clamp_score(starting_score - (wrong_guesses * penalty))


def get_hint(secret_number, guess):
    difference = abs(secret_number - guess)

    if difference == 0:
        return "Correct!"
    if difference <= 2:
        return "Very Close!"

    if guess < secret_number:
        return "Too Low" if difference <= 10 else "Much Lower"
    return "Too High" if difference <= 10 else "Much Higher"


def render_lives(lives_left, total_lives):
    filled = "\u2665" * lives_left
    empty = "\u2661" * (total_lives - lives_left)
    return filled + empty
