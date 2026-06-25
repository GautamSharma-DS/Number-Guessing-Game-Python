from dataclasses import dataclass, field


@dataclass
class Player:
    name: str = "Player"
    guess_history: list[int] = field(default_factory=list)

    def add_guess(self, guess: int):
        self.guess_history.append(guess)
