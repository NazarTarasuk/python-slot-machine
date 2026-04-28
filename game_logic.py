import random
from typing import Tuple

class SlotMachine:
    def __init__(self):
        self.symbols = ["🍒", "🍋", "🔔", "⭐"]

    def spin(self) -> Tuple[str, str, str]:
        """Видає три випадкові символи."""
        return (
            random.choice(self.symbols),
            random.choice(self.symbols),
            random.choice(self.symbols)
        )

    def calculate_win(self, s1: str, s2: str, s3: str, bet: int) -> int:
        """Рахує, скільки грошей виграв гравець."""
        if s1 == s2 == s3:
            return bet * 10  # Джекпот
        elif s1 == s2 or s2 == s3 or s1 == s3:
            return bet * 2   # Малий виграш
        return 0             # Програш