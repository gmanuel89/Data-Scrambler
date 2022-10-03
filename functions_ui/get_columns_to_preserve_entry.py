## Import libraries and functions
import tkinter
from tkinter import font

## Number of chunks entry
def get_columns_to_preserve_entry(window, ui_fonts: dict[str,font.Font], default_value: str) -> tkinter.Entry:
    columns_to_preserve_entry = tkinter.Entry(window, justify="center", width=50, font=ui_fonts.get('entry_font'))
    columns_to_preserve_entry.insert(0, default_value)
    columns_to_preserve_entry.grid(row=1, column=1, padx = 2, pady = 2)
    return columns_to_preserve_entry