#!/usr/bin/env python3
"""
Text-based Hangman Game with ASCII art.
Run: python hangman_game.py
"""
import random
from ascii_art import HANGMAN_STAGES
from words import WORDS


MAX_WRONG_GUESSES = 6  # lose on the 6th wrong guess


def display_word_state(word: str, guessed: set[str]) -> str:
    """Return the masked word with underscores for unguessed letters."""
    return " ".join(letter if letter in guessed else "_" for letter in word)


def play_one_round() -> None:
    """Play a single round of Hangman."""
    word = random.choice(WORDS)
    guessed_letters: set[str] = set()
    wrong_guesses = 0
    used_letters: list[str] = []

    print("🎯 Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while wrong_guesses <= MAX_WRONG_GUESSES:
        print("\n" + HANGMAN_STAGES[wrong_guesses])
        print("Word:   ", display_word_state(word, guessed_letters))
        print("Used:   ", " ".join(sorted(used_letters)) if used_letters else "(none)")
        print(f"Wrong:   {wrong_guesses}/{MAX_WRONG_GUESSES}")

        guess = input("Guess a letter: ").strip().lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single alphabet letter.")
            continue
        if guess in used_letters:
            print("ℹ️  You already tried that letter.")
            continue

        # Record the guess
        used_letters.append(guess)

        if guess in word:
            guessed_letters.add(guess)
            print(f"✅ Nice! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"❌ Nope! '{guess}' is not in the word.")

        # Win condition: all letters guessed
        if all(ch in guessed_letters for ch in word):
            print("\n🎉 You win!")
            print("The word was:", word)
            return

        # Lose condition handled by loop bound (prints final stage next)

        if wrong_guesses > MAX_WRONG_GUESSES:
            break

    # If we exit the loop, the player has lost
    print("\n" + HANGMAN_STAGES[-1])
    print("💀 Game over! The word was:", word)


def main() -> None:
    while True:
        play_one_round()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
