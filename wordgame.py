from wordclass import Word


word = Word()
all_letter_words = word.word_list
random_word = word.random_word
first_letter = word.first_letter

print(random_word)
print(first_letter)
print(all_letter_words)

while True:
    user_word = str(input('Guess a 5 letter word : '))
    if len(user_word) == 5 and user_word == random_word:
        print(user_word)
        break
