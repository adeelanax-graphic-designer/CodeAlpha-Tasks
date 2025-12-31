import random

def hangman():
    # Predefined word list
    words = ["apple", "banana", "orange", "grape", "mango"]

    # Choose a random word
    secret_word = random.choice(words)
    display_word = ["_"] * len(secret_word)
    guessed_letters = []
    attempts = 6

    print("🎮 Welcome to Hangman!")
    print("Guess the word, one letter at a time or try the full word!")

    # Main game loop
    while attempts > 0 and "_" in display_word:
        print("\nWord:", " ".join(display_word))
        print("Guessed letters:", ", ".join(guessed_letters))
        print("Attempts left:", attempts)

         #lower() will return the copy of the string converted into lowercase
        guess = input("Enter a letter or guess the full word: ").lower()    

        # Full word guess
        if len(guess) > 1:
            if guess == secret_word:
                display_word = list(secret_word)  # Reveal full word
                break  # Player wins
            else:
                print(" Wrong guess!")
                attempts -= 1
                continue

        # Single letter validation
        if not guess.isalpha() or len(guess) != 1:
            print(" Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print(" You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Correct guess
        if guess in secret_word:
            print("Good guess!")
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display_word[i] = guess
        else:
            print(" Wrong guess!")
            attempts -= 1

    # Game result
    if "_" not in display_word:
        print("\n Congratulations! You guessed the word:", secret_word)
    else:
        print("\n Game Over! The word was:", secret_word)

# Run the game
hangman()
