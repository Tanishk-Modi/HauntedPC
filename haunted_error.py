import tkinter as tk
from tkinter import messagebox
import random
import time

popup_options = [
    {"type": "error", "title": "System Alert", "message": "ERROR: YOU SHOULDN'T BE ALIVE"},
]

def perform_haunted_error():
    chosen_popup = random.choice(popup_options)
    popup_type = chosen_popup["type"]
    popup_title = chosen_popup["title"]
    popup_message = chosen_popup["message"]

    root = tk.Tk()
    root.withdraw()

    # Display the message box based on its type
    if popup_type == "error":
        messagebox.showerror(title=popup_title, message=popup_message)
    else:
        # Default to info if type is unrecognized
        messagebox.showinfo(title=popup_title, message=popup_message)
    
    root.destroy()