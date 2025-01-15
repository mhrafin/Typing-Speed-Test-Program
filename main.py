import tkinter as tk
from tkinter import Text, ttk

import darkdetect
import sv_ttk

root = tk.Tk()
sv_ttk.set_theme(darkdetect.theme())

# Window setup
root.title("Typing Speed Test")
mainframe = ttk.Frame(root, padding="3 3 12 12", height=720, width=1280)
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Test time
timer_label = ttk.Label(mainframe, text="00")
timer_label.grid(column=0, row=0, columnspan=3 , sticky=(tk.W))
time_count_label = ttk.Label(mainframe, text="Time")
time_count_label.grid(column=0, row=0, columnspan=3)
fifteen_sec_time_test_btn = ttk.Button(mainframe, text="15s")
fifteen_sec_time_test_btn.grid(column=1, row=1, sticky=(tk.W))

thirty_sec_time_test_btn = ttk.Button(mainframe, text="30s")
thirty_sec_time_test_btn.grid(column=1, row=1)

sixty_sec_time_test_btn = ttk.Button(mainframe, text="60s")
sixty_sec_time_test_btn.grid(column=1, row=1, sticky=(tk.E))

# Display test text
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
test_text = ttk.Label(mainframe, text=text, wraplength=1000, justify="center", font=("consolas", 28))
test_text.grid(column=0, row=2, columnspan=3)

# Type here
text_box = ttk.Entry(mainframe, width=50, font=("consolas", 20))
text_box.grid(column=0, row=3, columnspan=3)

# Reset
reset_btn = ttk.Button(mainframe, text="Reset")
reset_btn.grid(column=0, row=4, columnspan=3)


# Padding for all
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=10)


root.mainloop()