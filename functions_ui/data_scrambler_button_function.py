## Import libraries and functions
import os, tkinter
from tkinter import Tk, messagebox
from functions.scramble_data_from_file import scramble_data_from_file
from functions.write_csv_file import write_csv_file
from functions_ui.get_columns_to_preserve_from_entry import get_columns_to_preserve_from_entry
import data_lake.global_variables
from data_lake.ui_constants import *

## Data Scrambler button
def data_scrambler_button_function(columns_to_preserve_entry: tkinter.Entry):
    # Get the list of columns to preserve
    columns_to_preserve = get_columns_to_preserve_from_entry(columns_to_preserve_entry)
    # Purge the content if left default
    if len(columns_to_preserve) > 0 and columns_to_preserve[0] == COLUMNS_TO_PRESERVE_DEFAULT_VALUE:
        columns_to_preserve = []
    # Retrieve values from the data lake
    input_file = data_lake.global_variables.input_file
    input_file_name = data_lake.global_variables.input_file_name
    output_folder = data_lake.global_variables.output_folder
    data_lake.global_variables.columns_to_preserve = columns_to_preserve 
    print('INPUT FILE: ' + input_file)
    print('INPUT FILE NAME: ' + input_file_name)
    print('OUTPUT FOLDER: ' + output_folder)
    print('COLUMNS TO PRESERVE: ' + str(columns_to_preserve))
    # Scramble data
    input_file_scrambled = scramble_data_from_file(input_file, columns_to_preserve)
    # Write output file
    os.chdir(output_folder)
    write_csv_file(input_file_scrambled, str(input_file_name + ' - SCRAMBLED' + '.csv'))
    # Success
    Tk().withdraw()
    messagebox.showinfo(title='Success!', message='The input file data has been successfully scrambled!')
