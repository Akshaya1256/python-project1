import random
import time
import os


def play_again():
    question = 'Do You want to play again? y = yes, n = no \n'
    play_game = input(question)
    while play_game.lower() not in ['y', 'n']:
        play_game = input(question)

    if play_game.lower() == 'y':
        return True
    else:
        return False


def hangman(word):
    display = '_' * len(word)
    count = 0
    limit = 5
    letters = list(word)
    guessed = []
    while count < limit:
        guess = input(f'Hangman Word: {display} Enter your guess: \n').strip()
        while len(guess) == 0 or len(guess) > 1:
            print('Invalid input. Enter a single letter\n')
            guess = input(
                f'Hangman Word: {display} Enter your guess: \n').strip()

        if guess in guessed:
            print('Oops! You already tried that guess, try again!\n')
            continue

        if guess in letters:
            letters.remove(guess)
            index = word.find(guess)
            display = display[:index] + guess + display[index + 1:]

        else:
            guessed.append(guess)
            count += 1
            if count == 1:
                time.sleep(1)
                print('   ___ \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '_|_\n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 2:
                time.sleep(1)
                print('   ___ \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '_|_\n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 3:
                time.sleep(1)
                print('   ___ \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |      \n'
                      '  |      \n'
                      '  |      \n'
                      '_|_\n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 4:
                time.sleep(1)
                print('   ___ \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |     O \n'
                      '  |      \n'
                      '  |      \n'
                      '_|_\n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 5:
                time.sleep(1)
                print('   ___ \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |     | \n'
                      '  |     O \n'
                      '  |    /|\ \n'
                      '  |    / \ \n'
                      '_|_\n')
                print('Wrong guess. You\'ve been hanged!!!\n')
                print(f'The word was: {word}')

        if display == word:
            print(f'Congrats! You have guessed the word \'{word}\' correctly!')
            break


def play_hangman():
    print('\nWelcome to Hangman\n')
    name1 = input('Enter Player 1\'s name: ')
    name2 = input('Enter Player 2\'s name: ')
    print(f'Hello {name1} and {name2}! Best of Luck!')
    time.sleep(1)
    print('The game is about to start!\nLet\'s play Hangman!')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    words_to_guess = [
        'image', 'film', 'promise', 'kids',
        'lungs', 'rhyme', 'plants', 'world', 'car', 'donkey', 'player', 'phrase', 'brazil'
    ]
    play = True
    while play:
        word1 = random.choice(words_to_guess)
        words_to_guess.remove(word1)  # Remove the word after it has been chosen
        print(f"\n{len(word1)} letter word for {name1}. Start guessing!\n")
        
        start_time_player1 = time.time()
        print(f"{name1}'s turn:")
        hangman(word1)
        end_time_player1 = time.time()

        word2 = random.choice(words_to_guess)
        words_to_guess.remove(word2)  # Remove the word after it has been chosen
        print(f"\n{len(word2)} letter word for {name2}. Start guessing!\n")
        
        start_time_player2 = time.time()
        print(f"{name2}'s turn:")
        hangman(word2)
        end_time_player2 = time.time()

        if end_time_player1 - start_time_player1 < end_time_player2 - start_time_player2:
            print(f"\n{name1} guessed faster than {name2}!")
        elif end_time_player1 - start_time_player1 > end_time_player2 - start_time_player2:
            print(f"\n{name2} guessed faster than {name1}!")
        else:
            print("\nBoth players took the same time to guess!")
        play=play_again()
        if not words_to_guess:  # If no words left, ask if players want to play again.
            play = play_again()
            if play:
                words_to_guess = [
                    'image', 'film', 'promise', 'kids',
                    'lungs', 'rhyme', 'plants', 'world', 'car', 'donkey', 'player', 'phrase', 'brazil'
                ]
    
    print('Thanks For Playing! We expect you back again!')
    exit()


if __name__ == '__main__':
    play_hangman()
