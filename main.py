import sys
import tkinter as tk
import risultato
import pprint
pprint.pprint(sys.path)

x = 1
'''
but_1 = ""
but_2 = ""
but_3 = ""
but_4 = ""
but_5 = ""
but_6 = ""
but_7 = ""
but_8 = ""
but_9 = ""



def chek():
    if but_1 == but_2 == but_3 == "X" or but_4 == but_5 == but_6 == "X" or but_7 == but_8 == but_9 == "X"\
            or but_1 == but_4 == but_7 == "X" or but_2 == but_5 == but_8 == "X" or but_3 == but_6 == but_9 == "X" \
            or but_3 == but_5 == but_7 == "X" or but_1 == but_5 == but_9 == "X":
        hod.config(text="")
        result = tk.Label(root, text="Фу лох! Крестики победили")
        result.place(x=150, y=50)
        button_1.config(state="disabled")
        button_2.config(state="disabled")
        button_3.config(state="disabled")
        button_4.config(state="disabled")
        button_5.config(state="disabled")
        button_6.config(state="disabled")
        button_7.config(state="disabled")
        button_8.config(state="disabled")
        button_9.config(state="disabled")
        return result
    elif but_1 == but_2 == but_3 == "O" or but_4 == but_5 == but_6 == "O" or but_7 == but_8 == but_9 == "O"\
            or but_1 == but_4 == but_7 == "O" or but_2 == but_5 == but_8 == "O" or but_3 == but_6 == but_9 == "O" \
            or but_3 == but_5 == but_7 == "O" or but_1 == but_5 == but_9 == "O":
        hod.config(text="")
        result = tk.Label(root, text="Фу лох! Нолики победили")
        result.place(x=150, y=50)
        button_1.config(state="disabled")
        button_2.config(state="disabled")
        button_3.config(state="disabled")
        button_4.config(state="disabled")
        button_5.config(state="disabled")
        button_6.config(state="disabled")
        button_7.config(state="disabled")
        button_8.config(state="disabled")
        button_9.config(state="disabled")
        return result
    elif but_1 and but_2 and but_3 and but_4 and but_5 and but_6 and but_7 and but_8 and but_9 is not None:
        hod.config(text="")
        result = tk.Label(root, text="Ничья!")
        result.place(x=150, y=50)
'''
def push_1():
    global but_1
    global x
    if x % 2 != 0:
        button_1.config(text="X", state="disabled")
        but_1 = "X"
        x += 1
        hod.config(text=f"Ход {x} Ходят нолики.")
    elif x % 2 == 0:
        button_1.config(text="O", state="disabled")
        but_1 = "O"
        x += 1
        hod.config(text=f"Ход {x} Ходят крестики.")
    risultato.chek()


def push_2():
    global but_2
    global x
    if x % 2 != 0:
        button_2.config(text="X", state="disabled")
        but_2 = "X"
        x += 1
        hod.config(text=f"Ход {x} Ходят нолики.")
    elif x % 2 == 0:
        button_2.config(text="O", state="disabled")
        but_2 = "O"
        x += 1
        hod.config(text=f"Ход {x} Ходят крестики.")
    risultato.chek()



def push_3():
    global but_3
    global x
    if x % 2 != 0:
        button_3.config(text="X", state="disabled")
        but_3 = "X"
        x += 1
        hod.config(text=f"Ход {x} Ходят нолики.")
    elif x % 2 == 0:
        button_3.config(text="O", state="disabled")
        but_3 = "O"
        x += 1
        hod.config(text=f"Ход {x} Ходят крестики.")
    risultato.chek()


def push_4():
    global but_4
    global x
    if x % 2 != 0:
        button_4.config(text="X", state="disabled")
        but_4 = "X"
        x += 1
        hod.config(text=f"Ход {x} Ходят нолики.")
    elif x % 2 == 0:
        button_4.config(text="O", state="disabled")
        but_4 = "O"
        x += 1
        hod.config(text=f"Ход {x} Ходят крестики.")
    risultato.chek()


def push_5():
    global but_5
    global x
    if x % 2 != 0:
        button_5.config(text="X", state="disabled")
        but_5 = "X"
        x += 1
        hod.config(text=f"Ход {x} Ходят нолики.")
    elif x % 2 == 0:
        button_5.config(text="O", state="disabled")
        but_5 = "O"
        x += 1
        hod.config(text=f"Ход {x} Ходят крестики.")
    risultato.chek()

def push_6():
    global but_6
    global x
    if x % 2 != 0:
        button_6.config(text="X", state="disabled")
        but_6 = "X"
        x += 1
        hod.config(text=f"Ход {x} Ходят нолики.")
    elif x % 2 == 0:
        button_6.config(text="O", state="disabled")
        but_6 = "O"
        x += 1
        hod.config(text=f"Ход {x} Ходят крестики.")
    risultato.chek()

def push_7():
    global but_7
    global x
    if x % 2 != 0:
        button_7.config(text="X", state="disabled")
        but_7 = "X"
        x += 1
        hod.config(text=f"Ход {x} Ходят нолики.")
    elif x % 2 == 0:
        button_7.config(text="O", state="disabled")
        but_7 = "O"
        x += 1
        hod.config(text=f"Ход {x} Ходят крестики.")
    risultato.chek()

def push_8():
    global but_8
    global x
    if x % 2 != 0:
        button_8.config(text="X", state="disabled")
        but_8 = "X"
        x += 1
        hod.config(text=f"Ход {x} Ходят нолики.")
    elif x % 2 == 0:
        button_8.config(text="O", state="disabled")
        but_8 = "O"
        x += 1
        hod.config(text=f"Ход {x} Ходят крестики.")
    risultato.chek()

def push_9():
    global but_9
    global x
    if x % 2 != 0:
        button_9.config(text="X", state="disabled")
        but_9 = "X"
        x += 1
        hod.config(text=f"Ход {x} Ходят нолики.")
    elif x % 2 == 0:
        button_9.config(text="O", state="disabled")
        but_9 = "O"
        x += 1
        hod.config(text=f"Ход {x} Ходят крестики.")
    risultato.chek()


root = tk.Tk()
root.title("Крестики нолики")
root.geometry("400x400")
root.resizable(False, False)

hod = tk.Label(root, text=f"Ход {x}. Ходят крестики")
hod.place(x=150, y=50)

button_1 = tk.Button(root, text="", width=6, height=3, relief=tk.GROOVE, command=push_1)
button_1.place(x=100, y=100)
button_2 = tk.Button(root, text="", width=6, height=3, relief=tk.GROOVE, command=push_2)
button_2.place(x=150, y=100)
button_3 = tk.Button(root, text="", width=6, height=3, relief=tk.GROOVE, command=push_3)
button_3.place(x=200, y=100)

button_4 = tk.Button(root, text="", width=6, height=3, relief=tk.GROOVE, command=push_4)
button_4.place(x=100, y=150)
button_5 = tk.Button(root, text="", width=6, height=3, relief=tk.GROOVE, command=push_5)
button_5.place(x=150, y=150)
button_6 = tk.Button(root, text="", width=6, height=3, relief=tk.GROOVE, command=push_6)
button_6.place(x=200, y=150)

button_7 = tk.Button(root, text="", width=6, height=3, relief=tk.GROOVE, command=push_7)
button_7.place(x=100, y=200)
button_8 = tk.Button(root, text="", width=6, height=3, relief=tk.GROOVE, command=push_8)
button_8.place(x=150, y=200)
button_9 = tk.Button(root, text="", width=6, height=3, relief=tk.GROOVE, command=push_9)
button_9.place(x=200, y=200)

root.mainloop()
