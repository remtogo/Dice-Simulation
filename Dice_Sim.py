import random

def roll_die():

    # Simulates rolling a fair 6-sided die.
    return random.randint(1, 6)

if __name__ == "__main__":
    # Say hello to the user
    print("Hello, welcome to the Dice Simulator.")

    # Get the number of rolls from the user
    while True:
        try:
            num_rolls = int(input("Enter how many dice rolls you want to make: "))
            if num_rolls >= 0:  # Ensure the number of rolls is non-negative
              break
            else:
                print("Please enter a non-negative number of rolls.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    rolls = [roll_die() for _ in range(num_rolls)]
    print(f"\nResults of {num_rolls} rolls:")
    print(rolls)

    # Calculate frequencies to verify fairness
    frequencies = {}
    for value in rolls:
        frequencies[value] = frequencies.get(value, 0) + 1
    print("\nFrequencies:")
    for value in sorted(frequencies):
        print(f"Number {value}: {frequencies[value]} times")