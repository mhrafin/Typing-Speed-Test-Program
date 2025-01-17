import random
import time
import tkinter as tk
from tkinter import StringVar, ttk

import darkdetect
import keyboard as kb
import pandas as pd
import sv_ttk

# Get word data
data = pd.read_csv("data/words.csv")
word_list = data["words"].tolist()

# Initial words
some_words = random.choices(word_list, k=10)


currently_checking = 0
words_typed = 0
spelled_wrong = 0

# Time
first_time = True


def enter_new_words():
    global some_words, currently_checking
    some_words = random.choices(word_list, k=10)
    currently_checking = 0

    for i, word in enumerate(test_words):
        word.grid()
        word.config(text=some_words[i], foreground="gray")
    test_words[0].configure(foreground="black")


def manage_words():
    global currently_checking, words_typed, spelled_wrong, result

    # Get the current word and check spelling
    word = some_words[currently_checking]
    try:
        test_words[currently_checking + 1].configure(foreground="black")
    except IndexError:
        print()

    if text_entry.get().split(" ")[-2] == word:
        # print(f"Entered correct word {text_entry.get().split(' ')[-2]} == {word}")

        # print(currently_checking)
        test_words[currently_checking].configure(foreground="green")
    else:
        test_words[currently_checking].configure(foreground="red")
        spelled_wrong += 1

    currently_checking += 1
    text_entry.delete(0, tk.END)
    # print(currently_checking, some_words.__len__())
    if currently_checking == some_words.__len__():
        # print("new words")
        enter_new_words()

    # Display word stats, Time typing, show result.
    words_typed += 1
    words_typed_var.set(f"Words Typed: {words_typed} | Spelled Wrong: {spelled_wrong}")
    # print(words_typed)
    if words_typed == words_needed:
        finished_typing = time.time()
        total = finished_typing - started_typing
        print(f"WPS: {int((words_typed / total) * 60)}")
        for i, word in enumerate(test_words):
            word.grid_remove()

        res = int((words_typed / total) * 60)
        result = ttk.Label(
            test_frame,
            text=f"WPM: {res}\nWords Spelled Wrong: {spelled_wrong}",
            justify="center",
            font=("consolas", 28, "bold"),
        )
        result.grid(column=0, row=0, columnspan=5)


def key_released(key):
    global first_time, started_typing
    # print(key)
    # if first time, Start Timer, else continue
    if first_time:
        first_time = False
        started_typing = time.time()

    if key.keysym == "space":
        manage_words()


def set_word_type_10():
    global words_needed
    words_needed = 10
    ten_word_test_btn.state(["disabled"])
    twentyfive_word_test_btn.state(["!disabled"])
    fifty_word_test_btn.state(["!disabled"])
    hundred_word_text_btn.state(["!disabled"])
    reset()


def set_word_type_25():
    global words_needed
    words_needed = 25
    ten_word_test_btn.state(["!disabled"])
    twentyfive_word_test_btn.state(["disabled"])
    fifty_word_test_btn.state(["!disabled"])
    hundred_word_text_btn.state(["!disabled"])
    reset()


def set_word_type_50():
    global words_needed
    words_needed = 50
    ten_word_test_btn.state(["!disabled"])
    twentyfive_word_test_btn.state(["!disabled"])
    fifty_word_test_btn.state(["disabled"])
    hundred_word_text_btn.state(["!disabled"])
    reset()


def set_word_type_100():
    global words_needed
    words_needed = 100
    ten_word_test_btn.state(["!disabled"])
    twentyfive_word_test_btn.state(["!disabled"])
    fifty_word_test_btn.state(["!disabled"])
    hundred_word_text_btn.state(["disabled"])
    reset()


def reset():
    global first_time, spelled_wrong, words_typed
    first_time = True
    spelled_wrong = 0
    words_typed = 0
    words_typed_var.set(f"Words Typed: {words_typed} | Spelled Wrong: {spelled_wrong}")
    try:
        result.destroy()
    except NameError:
        print()
    enter_new_words()


root = tk.Tk()
sv_ttk.set_theme(darkdetect.theme())

# Window setup
root.title("Typing Speed Test")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# word
words_typed_var = StringVar()
words_typed_label = ttk.Label(mainframe, textvariable=words_typed_var)
words_typed_label.grid(column=0, row=0, columnspan=3, sticky=(tk.W))
word_count_label = ttk.Label(mainframe, text="Words")
word_count_label.grid(column=0, row=0, columnspan=4, sticky=(tk.S))


ten_word_test_btn = ttk.Button(mainframe, width=13, text="10", command=set_word_type_10)
ten_word_test_btn.grid(column=1, row=1, sticky=(tk.W))

twentyfive_word_test_btn = ttk.Button(
    mainframe, width=13, text="25", command=set_word_type_25
)
twentyfive_word_test_btn.grid(column=1, row=1, sticky=(tk.E))

fifty_word_test_btn = ttk.Button(
    mainframe, width=13, text="50", command=set_word_type_50
)
fifty_word_test_btn.grid(column=2, row=1, sticky=(tk.W))

hundred_word_text_btn = ttk.Button(
    mainframe, width=13, text="100", command=set_word_type_100
)
hundred_word_text_btn.grid(column=2, row=1, sticky=(tk.E))

# Display test text
test_frame = ttk.Frame(mainframe, padding="3 3 12 12")
test_frame.grid(column=0, row=2, columnspan=4)
mainframe.grid_rowconfigure(2, minsize=115)
mainframe.grid_columnconfigure((0, 1, 2, 3), minsize=300)

test_words = []
for n in range(0, 10):
    word = ttk.Label(
        test_frame,
        text=some_words[n],
        wraplength=1000,
        justify="center",
        font=("consolas", 28, "bold"),
        foreground="gray",
    )
    if n > 4:
        word.grid(column=n - 5, row=1)
        test_words.append(word)
        continue
    word.grid(column=n, row=0)
    test_words.append(word)

test_words[0].configure(foreground="black")

for child in test_frame.winfo_children():
    child.grid_configure(padx=10, pady=5)

# Type here
text_var = StringVar()
text_entry = ttk.Entry(mainframe, textvariable=text_var, font=("consolas", 20))
text_entry.grid(column=0, row=3, columnspan=4)
text_entry.bind("<KeyRelease>", key_released)


# Reset
reset_btn = ttk.Button(mainframe, text="Reset", command=reset)
reset_btn.grid(column=0, row=4, columnspan=4)


# Padding for all
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=10)


set_word_type_10()

root.mainloop()
