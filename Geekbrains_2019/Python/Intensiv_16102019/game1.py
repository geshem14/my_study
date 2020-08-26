import random

words_list = ('автострада', 'бензин', 'инопланетянин', 'самолет',
              'библиотека', 'шайба', 'олимпиада', 'осень', 'водопад')

secret_word = random.choice(words_list)
# print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

# gamer_word[2] = 'т'
# # immutable vs mutable
# print(''.join(gamer_word))

errors_counter = 0
while True:
    letter = input('введите ОДНУ русскую букву: ')
    if len(letter) != 1 or not letter.isalpha():
        continue
    # ord(letter)
    if letter in secret_word:
        for idx, symbol in enumerate(secret_word):
            # gamer_word[2] = 'т'
            # print(idx, symbol)
            if symbol == letter:
                gamer_word[idx] = letter
        if '*' not in gamer_word:
            print('\t\tвы выиграли!!!')
            break
    else:
        errors_counter += 1
        print('\tошибок допущено', errors_counter)
        if errors_counter == 8:
            print('\t\tвы проиграли ;(')
            break

    print(''.join(gamer_word))

print('до встречи')
