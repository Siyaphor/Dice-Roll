import random

def roll_dice():
    dice_face = random.randint(1, 6)
    dice_art = {
        1: ("⚀", "You rolled a 1!"),
        2: ("⚁", "You rolled a 2!"),
        3: ("⚂", "You rolled a 3!"),
        4: ("⚃", "You rolled a 4!"),
        5: ("⚄", "You rolled a 5!"),
        6: ("⚅", "You rolled a 6!"),
    }
    print(f"\n🎲 {dice_art[dice_face][0]}  →  {dice_art[dice_face][1]}")

def main():
    print("🎲 Welcome to the Dice Rolling Game!")
    while True:
        input("\nPress ENTER to roll the dice... ")
        roll_dice()

        again = input("Roll again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    main()
