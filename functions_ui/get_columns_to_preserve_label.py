## Import libraries and functions
import tkinter
from tkinter import font

## Columns to preserve label
def get_columns_to_preserve_label(window: tkinter.Tk, text_to_display: str, ui_fonts: dict[str,font.Font], ui_coordinates: tuple) -> tkinter.Label:
    columns_to_preserve_label = tkinter.Label(window, text=text_to_display, background="white", width=30, font=ui_fonts.get('label_font'))
    columns_to_preserve_label.grid(row=ui_coordinates[0], column=ui_coordinates[1], padx = 2, pady = 2)
    return columns_to_preserve_label