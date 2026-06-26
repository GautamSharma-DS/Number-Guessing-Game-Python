# Contributing

Thank you for your interest in contributing to the Advanced Number Guessing Game.

Please read this guide before submitting any changes.

This project is a Python terminal game with difficulty levels, lives, hints,
scoring, leaderboard, saved statistics, and unit tests.

## How to Contribute

1. Fork the repository.
2. Clone your fork.
3. Create a new branch.
4. Make your changes.
5. Run the game.
6. Run the tests.
7. Commit with a clear message.
8. Open a pull request.

## Branch Naming

Use clear branch names:

```text
feature/leaderboard
feature/gui-version
bugfix/input-validation
docs/update-readme
test/score-manager
```

## Run the Game

```bash
python -m src.main
```

Alternative:

```bash
python src/main.py
```

## Run Tests

```bash
pytest
```

## Code Style

- Write clean and readable Python code.
- Use meaningful names for variables, functions, and classes.
- Keep game logic separate from UI display code.
- Avoid unnecessary dependencies.
- Add comments only when they make the code easier to understand.
- Follow the existing project structure.

## Project Structure

```text
Project/
|
|-- src/
|   |-- main.py
|   |-- game.py
|   |-- config.py
|   |-- player.py
|   |-- score_manager.py
|   |-- sound_manager.py
|   |-- ui.py
|   |-- utils.py
|
|-- data/
|   |-- scores.json
|   |-- stats.json
|
|-- tests/
|   |-- test_game.py
|   |-- test_score.py
|
|-- docs/
|   |-- features.md
|
|-- assets/
|   |-- images/
|   |-- sounds/
```

## Good Contribution Ideas

- Improve terminal UI formatting.
- Add more unit tests.
- Improve input validation messages.
- Add more difficulty modes.
- Improve leaderboard display.
- Add optional sound files in `assets/sounds/`.
- Add more screenshots in `assets/images/`.
- Improve documentation examples.
- Fix bugs.
- Improve performance.
- Improve documentation.

## Data File Rules

Keep repository data clean before committing.

`data/scores.json` should start as:

```json
[]
```

`data/stats.json` should start as:

```json
{
    "games_played": 0,
    "games_won": 0,
    "games_lost": 0,
    "best_score": 0,
    "total_guesses": 0
}
```

Do not commit personal gameplay history unless it is intentionally added as
sample data.

## Commit Message Examples

Good commit messages:

```text
Add leaderboard feature
Fix invalid input handling
Improve README documentation
Add tests for score manager
```

Avoid unclear messages:

```text
update
changes
fix
new
```

## Pull Request Checklist

Before opening a pull request, make sure:

- The game runs successfully.
- Tests pass.
- README is still accurate.
- No virtual environment files are committed.
- No `__pycache__` files are committed.
- Data files are clean.
- New features are documented.
