import os

SAVE_FILE = "save.txt"
DEFAULT_BALANCE = 1000

def load_balance() -> int:
    """Завантажує баланс. Якщо файлу немає — дає 1000 монет."""
    if not os.path.exists(SAVE_FILE):
        return DEFAULT_BALANCE
    
    try:
        with open(SAVE_FILE, "r") as f:
            return int(f.read().strip())
    except (ValueError, IOError):
        return DEFAULT_BALANCE

def save_balance(balance: int) -> None:
    """Записує число балансу у файл."""
    try:
        with open(SAVE_FILE, "w") as f:
            f.write(str(balance))
    except IOError as e:
        print(f"Помилка запису: {e}")