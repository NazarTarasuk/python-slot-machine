from game_logic import SlotMachine
import storage

def run_game():
    # Завантажуємо баланс при старті
    balance = storage.load_balance()
    machine = SlotMachine()

    print("🎰 ЛАСКАВО ПРОСИМО В КАЗИНО!")

    while balance > 0:
        print(f"\nВаш баланс: {balance} грн")
        cmd = input("Введіть ставку (або 'q' для виходу): ")

        if cmd.lower() == 'q':
            break

        if not cmd.isdigit():
            print("❌ Введіть число!")
            continue

        bet = int(cmd)

        if bet > balance:
            print("❌ У вас немає стільки грошей!")
            continue
        if bet <= 0:
            print("❌ Ставка має бути більше нуля!")
            continue

        # Процес гри
        balance -= bet
        s1, s2, s3 = machine.spin()
        win = machine.calculate_win(s1, s2, s3, bet)

        print(f"| {s1} | {s2} | {s3} |")

        if win > 0:
            print(f"🥳 ВИГРАШ: {win} грн!")
            balance += win
        else:
            print("😢 Програш...")

        # Зберігаємо після кожного ходу
        storage.save_balance(balance)

    print(f"\nГру завершено! Ви пішли з: {balance} грн")

if __name__ == "__main__":
    run_game()