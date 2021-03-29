import tkinter as tk
from tkinter import messagebox

move = 0
click = True
game = tk.Tk()
game.title('Tic Tac Toe')
current = []
buttons = []

def create_button(x, y):
    button = tk.Button(width=10, text='', height=5, command=lambda: callback(button))
    button.grid(row=x, column=y)
    print(button['text'])
    return button

def check_win():
    global ans
    ans = ''
    if (buttons[0]['text'] == buttons[1]['text'] == buttons[2]['text'] != '') or \
            (buttons[3]['text'] == buttons[4]['text'] == buttons[5]['text'] != '') or \
            (buttons[6]['text'] == buttons[7]['text'] == buttons[8]['text'] != '') or \
            (buttons[0]['text'] == buttons[3]['text'] == buttons[6]['text'] != '') or \
            (buttons[1]['text'] == buttons[4]['text'] == buttons[7]['text'] != '') or \
            (buttons[2]['text'] == buttons[5]['text'] == buttons[8]['text'] != '') or \
            (buttons[2]['text'] == buttons[4]['text'] == buttons[6]['text'] != '') or \
            (buttons[0]['text'] == buttons[4]['text'] == buttons[8]['text'] != ''):
        ans = messagebox.askyesno('WINNER !', str(current[-1]) + ' is a winner ! \n Play Again ?')

    elif move == 9:
        ans = messagebox.askyesno('TIE !', 'There\'s is no winner in this round \n Play Again ?')

    reset_game()

def reset_game():
    global ans, move, current, buttons, click
    if ans == True:
        ans = ''
        move = 0
        current = []
        buttons = []
        click = True
        main()
    elif ans == False:
        game.destroy()


def callback(btn):
    global move, click, ans

    if btn['text'] == '' and click :
        btn['text'] = 'X'
        current.append(btn['text'])
        click = False
        move += 1
    elif btn['text'] == '' and not click:
        btn['text'] = 'O'
        current.append(btn['text'])
        click = True
        move += 1
    print(current)
    check_win()

def main():
    for i in range(9):
        row = i // 3
        col = i % 3
        buttons.append(create_button(row, col))

main()
game.mainloop()