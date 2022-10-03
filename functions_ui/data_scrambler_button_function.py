## Import libraries and functions
import os
from tkinter import Tk, messagebox
from functions.scramble_data_from_file import scramble_data_from_file
from functions.write_csv_file import write_csv_file
import data_lake.global_variables

## Data Scrambler button
def data_scrambler_button_function():
    input_file = data_lake.global_variables.input_file
    input_file_name = data_lake.global_variables.input_file_name
    output_folder = data_lake.global_variables.output_folder
    print('INPUT FILE: ' + input_file)
    print('INPUT FILE NAME: ' + input_file_name)
    print('OUTPUT FOLDER: ' + output_folder)
    # Scramble data
    input_file_scrambled = scramble_data_from_file(input_file)
    # Write output file
    os.chdir(output_folder)
    write_csv_file(input_file_scrambled, str(input_file_name + ' - SCRAMBLED' + '.csv'))
    # Success
    Tk().withdraw()
    messagebox.showinfo(title='Success!', message='The input file data has been successfully scrambled!')
