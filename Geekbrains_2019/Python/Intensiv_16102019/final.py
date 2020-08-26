import random
import tkinter
from tkinter import messagebox

G_HEIGHT = 400
G_WIDTH = 800

game_started = False

main_window = tkinter.Tk()
main_window.title('игра')

real_h, real_w = main_window.winfo_screenheight(), main_window.winfo_screenwidth()

left_offset = (real_w - G_WIDTH) // 2
top_offset = (real_h - G_HEIGHT) // 2

main_window.geometry(f'{G_WIDTH}x{G_HEIGHT}+{left_offset}+{top_offset}')
main_window.iconbitmap('game.ico')
main_window.resizable(width=False, height=False)
# main_window.configure(background='#eeeeee')
main_window['bg'] = '#eeeeee'

var_gamer_word = tkinter.StringVar()
var_mistakes_else = tkinter.StringVar()

label_1 = tkinter.Label(main_window, text='угадайте слово')
label_1.config(font=("Courier", 16))
label_1.place(x=0, y=0)

label_2 = tkinter.Label(main_window, textvariable=var_gamer_word)
label_2.config(font=("Courier", 28))
label_2.place(x=0, y=G_HEIGHT // 3)

label_3 = tkinter.Label(main_window, textvariable=var_mistakes_else)
label_3.config(font=("Courier", 14))
label_3.place(x=0, y=G_HEIGHT // 3 * 2)


def new_game():
    global secret_word, gamer_word, mistakes_else, used_letters, game_started, game_finished
    words = ['помидор', 'сноуборд', 'пианино', 'афиша', 'автобус', 'пустыня']

    secret_word = random.sample(words, 1)[0]

    gamer_word = ['*'] * len(secret_word)
    var_gamer_word.set(''.join(gamer_word))

    mistakes_else = 8
    used_letters = []
    game_started = True
    game_finished = False

    var_mistakes_else.set("")


def exit_game():
    exit(0)


button_1 = tkinter.Button(main_window, text='заново', command=new_game,
                          bg='gray', fg='blue')
button_1.config(font=("Courier", 16))
button_1.place(x=0, y=G_HEIGHT - 50)
button_2 = tkinter.Button(main_window, text='выход', command=exit_game,
                          bg='gray', fg='blue')
button_2.config(font=("Courier", 16))
button_2.place(x=G_WIDTH // 2, y=G_HEIGHT - 50)

if not game_started:
    new_game()


def check_letter(letter):
    if len(letter) == 1 and 1072 <= ord(
            letter) <= 1103 and letter not in used_letters:
        used_letters.append(letter)
        return True
    elif len(letter) != 1:
        print(f'вы ввели больше одного символа!')
    elif letter in used_letters:
        print(f'буква "{letter}" уже была!')
    elif not letter.isalpha():
        print(f'"{letter}" не буква!')
    else:
        print(f'буква "{letter}" не из русского алфавита!')

    return False


def check_win(gamer_word):
    if mistakes_else == 0:
        messagebox.showinfo('Увы', 'Вы проиграли')

    if '*' in gamer_word:
        return False
    else:
        messagebox.showinfo('Ура', 'Вы выиграли')

    return True


def key_press(arg):
    global mistakes_else, game_finished

    if game_finished:
        return

    letter = arg.char.lower()

    if used_letters:
        var_mistakes_else.set(
            f"запас {mistakes_else}, пробовали буквы: {' '.join(used_letters)}")

    print(secret_word)
    if check_letter(letter):
        if letter in secret_word:
            for pos, char in enumerate(secret_word):
                if char == letter:
                    gamer_word[pos] = letter

            var_gamer_word.set(''.join(gamer_word))
        else:
            mistakes_else -= 1

    game_finished = check_win(gamer_word)


main_window.bind('<KeyPress>', key_press)

main_window.mainloop()
