# Features

## Gameplay

- Welcome screen with difficulty selection
- Player name input before each game
- Easy, Medium, and Hard modes
- Random number generation for each round
- Limited lives based on difficulty
- Guess counter and previous guess history
- Play again option after each round
- Leaderboard for top winning scores
- Reset option for saved scores and statistics

## Hints

- `Very Close!` for guesses within 2 numbers
- `Too Low` when the guess is below the answer but nearby
- `Too High` when the guess is above the answer but nearby
- `Much Lower` when the guess is far below the answer
- `Much Higher` when the guess is far above the answer

## Scoring

- Starts at 100 points
- Every wrong guess reduces score by 10
- Best score is saved across runs
- Top winning scores and player names are stored in `data/scores.json`

## Statistics

- Games played
- Games won
- Games lost
- Win rate
- Best score
- Average guesses

## Sound

- Uses Windows terminal beep effects when `winsound` is available
- Runs normally without sound on unsupported systems
