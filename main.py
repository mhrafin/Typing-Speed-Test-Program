import random
import tkinter as tk
from tkinter import StringVar, Text, ttk

import darkdetect
import keyboard as kb
import pandas as pd
import sv_ttk

data = pd.read_csv("data/words.csv")
word_list = data["words"].tolist()

some_words = random.choices(word_list, k=5)


currently_checking = 0


def enter_new_words():
    global some_words, currently_checking
    some_words = random.choices(word_list, k=5)
    currently_checking = 0

    for i, word in enumerate(test_words):
        word.config(text=some_words[i], foreground="gray")
    test_words[0].configure(foreground="black")

def manage_words():
    global currently_checking

    # current_index = text_entry.get().split(" ")[-1].__len__() - 1

    word = some_words[currently_checking]
    # test_words[currently_checking-1].configure(foreground="gray")
    try:
        test_words[currently_checking+1].configure(foreground="black")
    except IndexError:
        print()

    if text_entry.get().split(" ")[-2] == word:
        print(f"Entered correct word {text_entry.get().split(' ')[-2]} == {word}")

        print(currently_checking)
        test_words[currently_checking].configure(foreground="green")
    else:
        test_words[currently_checking].configure(foreground="red")

    currently_checking += 1
    text_entry.delete(0, tk.END)
    print(currently_checking, some_words.__len__())
    if currently_checking == some_words.__len__():
        print("new words")
        enter_new_words()


def print_key(key):
    # print(key)
    # if first time, Start Timer, else continue

    if key.keysym == "space":
        manage_words()


root = tk.Tk()
style = ttk.Style()
style.configure("Green.TLabel", foreground="green")
sv_ttk.set_theme(darkdetect.theme())

# Window setup
root.title("Typing Speed Test")
mainframe = ttk.Frame(root, padding="3 3 12 12", height=720, width=1280)
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Test time
timer_label = ttk.Label(mainframe, text="00")
timer_label.grid(column=0, row=0, columnspan=3, sticky=(tk.W))
time_count_label = ttk.Label(mainframe, text="Time")
time_count_label.grid(column=0, row=0, columnspan=3, sticky=(tk.S))
fifteen_sec_test_btn = ttk.Button(mainframe, text="15s")
fifteen_sec_test_btn.grid(column=1, row=1, sticky=(tk.W))

thirty_sec_test_btn = ttk.Button(mainframe, text="30s")
thirty_sec_test_btn.grid(column=1, row=1)

sixty_sec_test_btn = ttk.Button(mainframe, text="60s")
sixty_sec_test_btn.grid(column=1, row=1, sticky=(tk.E))

# Display test text
test_frame = ttk.Frame(mainframe, padding="3 3 12 12")
test_frame.grid(column=0, row=2, columnspan=3)

test_words = []
for n in range(0, 5):
    word = ttk.Label(
        test_frame,
        text=some_words[n],
        wraplength=1000,
        justify="center",
        font=("consolas", 28, "bold"),
        foreground="gray",
    )
    word.grid(column=n, row=0)
    test_words.append(word)

test_words[0].configure(foreground="black")

for child in test_frame.winfo_children():
    child.grid_configure(padx=10, pady=5)

# Type here
text_var = StringVar()
text_entry = ttk.Entry(mainframe, textvariable=text_var, font=("consolas", 20))
text_entry.grid(column=0, row=3, columnspan=3)
text_entry.bind("<KeyRelease>", print_key)


# Reset
reset_btn = ttk.Button(mainframe, text="Reset")
reset_btn.grid(column=0, row=4, columnspan=3)


# Padding for all
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=10)


root.mainloop()
