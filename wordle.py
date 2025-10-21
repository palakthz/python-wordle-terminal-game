import random
import sys
from collections import defaultdict

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    GRAY = Fore.LIGHTBLACK_EX
    RESET = Style.RESET_ALL
except ImportError:
    print("For a better experience with colors, please install the 'colorama' library.")
    print("You can do this by running: pip install colorama")
    GREEN = YELLOW = GRAY = RESET = ""



WORD_LENGTH = 5
MAX_ATTEMPTS = 6

# --- Word List ---
WORD_LIST = [
    "apple", "baker", "crane", "drift", "eager", "fable", "grape", "haste",
    "image", "jolly", "knife", "lemon", "mango", "night", "ocean", "pearl",
    "query", "roast", "smile", "table", "unity", "vigor", "waste", "xenon",
    "yacht", "zebra", "abuse", "beach", "cloud", "dream", "earth", "faith",
    "ghost", "heart", "ivory", "juice", "light", "money", "noise", "order",
    "peace", "quiet", "river", "shade", "thing", "ultra", "voice", "world",
    "youth", "zesty", "album", "blush", "charm", "drive", "empty", "flame",
    "grasp", "honor", "inbox", "joint", "kneel", "lucky", "march", "noble",
    "offer", "pilot", "queen", "raven", "spice", "tiger", "urban", "vivid",
    "wheat", "yield", "angel", "brick", "craft", "daisy", "equal", "feast",
    "glory", "harsh", "irony", "jewel", "karma", "lodge", "mirth", "nurse",
    "orbit", "pride", "risky", "scent", "treat", "umbra", "vapor", "witty",
    "xerox", "young", "zonal", "amber", "blink", "crown", "delta", "eagle",
    "flock", "grind", "haven", "index", "judge", "laser", "metal", "nerve",
    "oasis", "piano", "quilt", "robin", "sweet", "truly", "vowel", "wider",
    "actor", "blend", "climb", "draft", "elbow", "frost", "grill", "hound",
    "input", "jumps", "knock", "loyal", "mover", "ninth", "overt", "pound",
    "rider", "sugar", "touch", "unite", "valor", "woven", "whale", "yield",
    "zippy", "adore", "bleak", "crisp", "dealt", "enter", "flair", "grief",
    "happy", "irate", "jumpy", "leash", "minor", "niche", "onset", "pluck",
    "quest", "rival", "sight", "tough", "under", "vital", "worry", "yummy",
    "amuse", "bloom", "chase", "diner", "enjoy", "froze", "gleam", "hurry",
    "ideal", "jolly", "knead", "linen", "motto", "noble", "olive", "petal",
    "ranch", "spine", "trend", "unfed", "vague", "weary", "xylem", "zonal"
]

def select_secret_word(word_list):
    """Selects a random word from the provided list."""
    return random.choice(word_list)


def print_welcome_message():
    """Prints the initial welcome message and instructions."""
    print("\n--- Welcome to Python Wordle! ---")
    print(f"Guess the {WORD_LENGTH}-letter word in {MAX_ATTEMPTS} tries.")
    print("Each guess must be a valid 5-letter word.")
    print("After each guess, the color of the letters will change to show how close your guess was.")
    print(f"  {GREEN}GREEN{RESET} means the letter is in the word and in the correct spot.")
    print(f"  {YELLOW}YELLOW{RESET} means the letter is in the word but in the wrong spot.")
    print(f"  {GRAY}GRAY{RESET} means the letter is not in the word in any spot.\n")


def get_user_guess():
    """Prompts the user for a guess and validates its format."""
    while True:
        guess = input("Enter your guess: ").lower().strip()
        if len(guess) != WORD_LENGTH:
            print(f"Oops! Your guess must be {WORD_LENGTH} letters long. Try again.")
        elif not guess.isalpha():
            print("Oops! Your guess must only contain letters. Try again.")
        else:
            return guess


def evaluate_guess(secret_word, guess):
    """
    Evaluates the user's guess and returns a colored feedback string.

    The logic carefully handles duplicate letters to match the official Wordle rules.
    1. First pass for GREEN matches.
    2. Second pass for YELLOW and GRAY matches.
    """
    if len(secret_word) != len(guess):
        raise ValueError("Secret word and guess must be of the same length.")

    feedback = [""] * WORD_LENGTH
    secret_word_letter_counts = defaultdict(int)

    # First pass: Find all correct letters in the correct position (GREEN)
    for i, letter in enumerate(guess):
        if secret_word[i] == letter:
            feedback[i] = GREEN + letter + RESET
        else:
            secret_word_letter_counts[secret_word[i]] += 1

    # Second pass: Find correct letters in wrong positions (YELLOW) and incorrect letters (GRAY)
    for i, letter in enumerate(guess):
        # Skip letters that are already marked as green
        if feedback[i]:
            continue

        if secret_word_letter_counts[letter] > 0:
            feedback[i] = YELLOW + letter + RESET
            secret_word_letter_counts[letter] -= 1
        else:
            feedback[i] = GRAY + letter + RESET

    return " ".join(feedback)


def play_game():
    """Main function to run the Wordle game loop."""
    secret_word = select_secret_word(WORD_LIST)
    attempts_left = MAX_ATTEMPTS
    guesses = []

    print_welcome_message()

    while attempts_left > 0:
        print(f"You have {attempts_left} attempt(s) remaining.")
        user_guess = get_user_guess()

        feedback = evaluate_guess(secret_word, user_guess)
        guesses.append(feedback)

        # Print all previous guesses
        print("\n--- Your Guesses ---")
        for g in guesses:
            print(g)
        print("--------------------\n")

        if user_guess == secret_word:
            print(f"Congratulations! You guessed the word '{secret_word}' correctly!")
            return

        attempts_left -= 1

    print(f"Game over! The secret word was '{secret_word}'. Better luck next time!")
    
#play again 

def play_again():
    """Asks the user if they want to play again."""
    while True:
        again = input("Would you like to play again? (y/n): ").lower().strip()
        if again == "y":
            play_game()
            break
        elif again == "n":
            print("Thanks for playing! Goodbye 👋")
            sys.exit()
        else:
            print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    play_game()
    play_again()
    """Asks the user if they want to play again."""