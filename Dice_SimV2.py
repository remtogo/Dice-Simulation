import random
from scipy.stats import chisquare
import matplotlib.pyplot as plt
import numpy as np

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
    if num_rolls > 0:
        observed_frequencies = [frequencies.get(i, 0) for i in range(1, 7)]
        expected_frequency = num_rolls / 6.0
        expected_frequencies = [expected_frequency] * 6
        chi_square, p_value = chisquare(observed_frequencies, expected_frequencies)

        print(f"\nChi-Square: {chi_square:.4f}")
        print(f"P-value: {p_value:.4f}")

    # Visualization
    plt.figure(figsize=(8, 6))
    probabilities = [freq / num_rolls for freq in frequencies.values()]
    plt.bar(frequencies.keys(), probabilities, alpha=0.7)
    plt.axhline(y=1 / 6, color='r', linestyle='--', label='Expected Probability (1/6)')
    plt.title('Observed Probabilities vs Expected')
    plt.xlabel('Roll Value')
    plt.ylabel('Probability')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Show visualization
    plt.show()