# Changelog

All notable changes to the Advanced Number Guessing Game are documented in this file.

## [1.0.0] - 2026-06-25

### Added

- Created the first complete version of the Number Guessing Game.
- Added difficulty levels:
  - Easy: range `1-20`, lives `8`.
  - Medium: range `1-50`, lives `6`.
  - Hard: range `1-100`, lives `5`.
- Added random number generation for every round.
- Added player name support.
- Added limited lives with heart-style display.
- Added guess counter.
- Added previous guess history.
- Added score system starting from `100` points.
- Added smart hint system:
  - `Very Close!`
  - `Too Low`
  - `Too High`
  - `Much Lower`
  - `Much Higher`
- Added win and game over screens.
- Added Play Again option.
- Added best score tracking.
- Added leaderboard support.
- Added game statistics:
  - Games played.
  - Games won.
  - Games lost.
  - Win rate.
  - Best score.
  - Average guesses.
- Added JSON persistence using:
  - `data/scores.json`
  - `data/stats.json`
- Added reset scores/statistics option.
- Added optional Windows terminal sound effects with `winsound`.
- Added pytest-based tests for game helper functions and score management.
- Added project documentation:
  - `README.md`
  - `docs/features.md`
  - `CONTRIBUTING.md`

### Changed

- Improved terminal menu formatting.
- Improved game status layout.
- Improved leaderboard and statistics display.
- Added Rich-powered terminal panels, tables, and styled messages.
- Cleaned saved data files for a portfolio-ready repository.
- Updated `.gitignore` for virtual environment, Python cache, VS Code, and environment files.
- Added README screenshot support using `assets/images/menu.png`.
- Added `assets/sounds/` folder for future sound files.

### Fixed

- Fixed Play Again flow so the player name is not asked again in the same session.
- Fixed repository data files to avoid committing personal gameplay history.

### Removed

- Removed unnecessary generated/local files from the repository.
- Removed unused placeholder assets that were not needed.
