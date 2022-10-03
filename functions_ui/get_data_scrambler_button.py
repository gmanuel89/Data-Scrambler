## Import libraries and functions
from functions_ui.data_scrambler_button_function import data_scrambler_button_function
import tkinter
from tkinter import font

def get_data_scrambler_button(window: tkinter.Tk, text_to_display: str, columns_to_preserve_entry: tkinter.Entry, ui_fonts: dict[str,font.Font]) -> tkinter.Button:
    data_scrambler_button = tkinter.Button(window, text=text_to_display, command=lambda: data_scrambler_button_function(columns_to_preserve_entry), background = "white", font=ui_fonts.get('button_font'))
    data_scrambler_button.grid(row=4, column=0, padx = 2, pady = 2)
    return data_scrambler_button