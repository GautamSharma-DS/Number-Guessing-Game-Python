# Number Guessing Game

A portfolio-ready Python terminal game with difficulty levels, lives, hints,
score tracking, best score, saved statistics, and optional Windows sound effects.

## Run

```bash
python -m src.main
```

or

```bash
python src/main.py
```

## Features

- Welcome screen
- Player name input
- Difficulty selection: Easy, Medium, Hard
- Random number generation
- Limited lives
- Guess counter
- Score system
- Smart hints
- Guess history
- Play again option
- Leaderboard
- Reset scores option
- Best score saved in JSON
- Game statistics saved in JSON
- Optional Windows terminal sound effects

## Difficulty

| Difficulty | Range | Lives |
| ---------- | ----- | ----- |
| Easy | 1 - 20 | 8 |
| Medium | 1 - 50 | 6 |
| Hard | 1 - 100 | 5 |

## Score Rules

- Start with 100 points
- Every wrong guess subtracts 10 points
- Score never goes below 0

## Hint Examples

If the correct number is `75`:

- Guess `73` shows `Very Close!`
- Guess `40` shows `Much Lower`
- Guess `95` shows `Much Higher`

## Menu

```text
1. Easy
2. Medium
3. Hard
4. View Statistics
5. View Leaderboard
6. Reset Scores
7. Exit
```

## Sample Game Status

```text
============================================
Lives Left : ♥♥♥♡♡
Guess No.  : 3
Score      : 80
Timer      : 12.4s
Previous   : 40, 95
============================================
```

## Data Files

- `data/scores.json` stores top winning scores and player names
- `data/stats.json` stores overall statistics

## Tests

```bash
python -m unittest discover tests
```
