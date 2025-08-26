import random

def play_hangman():
    words = ['apple', 'mango', 'grape', 'peach', 'berry']
    secret_word = random.choice(words)
    guessed_letters = []    
    wrong_attempts = 0      
    max_wrong = 6           
    print("Welcome to Hangman!")
    print(f"You can make up to {max_wrong} wrong guesses. Let's go!\n")

    while True:
        display = ''
        for ch in secret_word:
            if ch in guessed_letters:
                display += ch + ' '
            else:
                display += '_ '
        print("Word:", display.strip())
        if all(ch in guessed_letters for ch in secret_word):
            print("\n🎉 Congratulations! You’ve guessed the word!")
            break
        print(f"Guesses left: {max_wrong - wrong_attempts}")
        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("  → Enter a single alphabet letter.\n")
            continue
        if guess in guessed_letters:
            print("  → You've already guessed that letter.\n")
            continue

        guessed_letters.append(guess)
        if guess in secret_word:
            print("  → Good guess!\n")
        else:
            wrong_attempts += 1
            print("  → Wrong guess.\n")
            if wrong_attempts >= max_wrong:
                print(f"\nYou’ve run out of guesses! The word was: '{secret_word}'.")
                break

if __name__ == "__main__":
    play_hangman()
