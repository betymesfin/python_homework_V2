def make_hangman(secret_word):
    guesses=[]
    def hangman_closure(letter):
        if letter not in guesses:
            guesses.append(letter)
        displayed = ''
        for char in secret_word:
            if char in guesses:
                displayed += char
            else:
                displayed += '_'
        print(displayed)
        for char in secret_word:
           if char not in guesses:
              return False
        return True

    return hangman_closure


secret_word = input("Enter the secret word: ").lower()
game = make_hangman(secret_word)

while True:
    guess = input("Guess a letter: ").lower()
    finished = game(guess)

    if finished:
        print(f"Congratulations! You guessed the word: {secret_word}")
        break