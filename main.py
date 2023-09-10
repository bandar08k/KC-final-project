import tkinter as tk
from tkinter import messagebox

game = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

def button_click(row, col):
    global current_player

    if game[row][col] == ' ':
        buttons[row][col].config(text=current_player)
        game[row][col] = current_player

        if check_win(current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = 'O' if current_player == 'X' else 'X'

def check_win(player):
    for row in game:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(game[row][col] == player for row in range(3)):
            return True

    if game[0][0] == game[1][1] == game[2][2] == player:
        return True
    if game[0][2] == game[1][1] == game[2][0] == player:
        return True

    return False

def check_draw():
    return all(cell != ' ' for row in game for cell in row)

def reset_game():
    global current_player, game

    game = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=' ')

window = tk.Tk()
window.title("X/O Game")

buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(window, text=' ', width=10, height=5,
                           command=lambda r=row, c=col: button_click(r, c))
        button.grid(row=row, column=col, padx=5, pady=5)
        button_row.append(button)
    buttons.append(button_row)

window.mainloop()