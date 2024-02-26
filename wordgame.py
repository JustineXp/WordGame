import re
from wordclass import Word

pattern = re.compile("[a-zA-Z]{5}")


word = Word()
all_letter_words = word.word_list
random_word = word.random_word
first_letter = word.first_letter

print(random_word)

while True:
    user_word = str(input('Guess a 5 letter word : ').strip())
    if bool(re.search("[^a-zA-Z]", user_word)):
        print('The word should have only letters, try again . . .')
    elif bool(pattern.search(user_word)):
        if user_word == random_word:
            print(f'Congratulations, {user_word} is the correct word.')
            confirmation = input('Could you wish to continue ? (yes/no) ')
            if confirmation == 'yes':
                word = Word()
                user_word = str(input('Guess a 5 letter word : ').strip())
            elif confirmation == 'no':
                break
            else:
                print('Use Yes or No only.')
        else:
            print('Sorry that is not correct. Try again. . .')
    else:
        print('The word Entered is not 5 Letters Long.')
