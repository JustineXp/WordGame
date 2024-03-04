import re
from wordclass import Word
import random
import time

pattern = re.compile("[a-zA-Z]{5}")
nums_pattern = re.compile("[0-9]{3}")
number_of_times = 1


def shuffled():
    word_list = []
    for _ in random_word:
        word_list.append(_.upper())
        random.shuffle(word_list)

    shuffled_letters = '-'.join(word_list)
    return shuffled_letters


def word_creation():
    word = Word()
    all_letter_words = word.word_list
    random_word = word.random_word.lower()
    first_letter = word.first_letter

    return first_letter, random_word, all_letter_words


def show_answer():
    time.sleep(5)
    print(f"CORRET ANSWER : {random_word.upper()}")


def fetch_input(user_string):
    return input(f'{user_string}[ {shuffled_letters} ] : ').strip().lower()


def fetch_confirmation():
    return str(input('Do you wish to continue ? (yes/no) ')).lower()


first_letter, random_word, all_letter_words = word_creation()
shuffled_letters = shuffled()


while True:
    user_word = fetch_input('GUESS A 5 LETTER WORD CONSISTING OF THE LETTERS ')
    if bool(re.search("[^a-zA-Z]", user_word)):
        print('USE ONLY LETTERS IN YOUR WORD . . .')
    elif bool(pattern.search(user_word)):
        if user_word == random_word:
            print(f'CONGRATULATIONS, {user_word} IS THE CORRECT WORD.')
            confirmation = fetch_confirmation()
            if confirmation == 'yes':
                first_letter, random_word, all_letter_words = word_creation()
                shuffled_letters = shuffled()
            elif confirmation == 'no':
                break
            else:
                while confirmation != 'yes' or confirmation != 'no':
                    print('Use Yes or No only.')
                    confirmation = fetch_confirmation()
                    if confirmation == 'yes':
                        first_letter, random_word, all_letter_words = word_creation()
                        shuffled_letters = shuffled()
                    elif confirmation == 'no':
                        break
        else:
            print('Sorry that is not correct. Try again. . .')
            # update times tracker
            number_of_times += 1
            if number_of_times > 3:
                number_of_time = 1
                print(f"The correct answer is : {random_word}")
                first_letter, random_word, all_letter_words = word_creation()
                shuffled_letters = shuffled()
            # once it reaces 3 times show the correct answer
    else:
        print('SORRY, THE WORD ENTER IS NOT A 5 LETTER WORD. \nTRY AGAIN . . .')
