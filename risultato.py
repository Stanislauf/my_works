
x = 1
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

