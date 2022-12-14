## Pre-requisites
from functions.install_required_packages import install_required_packages
install_required_packages(['pandas'])

## Initialisation
from data_lake.constants import *
import data_lake.global_variables
from data_lake.ui_constants import *

## Import functions
from functions_ui import *

## Import libraries
import tkinter

## Initialise variables
output_folder = data_lake.global_variables.output_folder
input_file = data_lake.global_variables.input_file
input_file_name = data_lake.global_variables.input_file_name

## WINDOW
### Main window
window = tkinter.Tk()
window.title("CSV splitter")
window.resizable(False, False)
window.configure(background = "white")
#window.wm_minsize(width=550, height=600)

# Get UI fonts
ui_fonts = get_ui_fonts(window)
#print(ui_fonts)

## UI elements
# Title / Info
get_title_label(window, TITLE_LABEL, GITHUB_WIKI_URL, ui_fonts, TITLE_LABEL_COORDINATES)
# Quit
get_quit_button(window, QUIT_BUTTON_LABEL, ui_fonts, QUIT_BUTTON_COORDINATES)
# Output folder
get_output_folder_button(window, OUTPUT_FOLDER_BUTTON_LABEL, ui_fonts, OUTPUT_FOLDER_BUTTON_COORDINATES)
get_output_folder_label(window, output_folder, ui_fonts, OUTPUT_FOLDER_LABEL_COORDINATES)
# Output folder
get_columns_to_preserve_label(window, COLUMNS_TO_PRESERVE_LABEL, ui_fonts, COLUMNS_TO_PRESERVE_LABEL_COORDINATES)
columns_to_preserve_entry = get_columns_to_preserve_entry(window, ui_fonts, COLUMNS_TO_PRESERVE_DEFAULT_VALUE, COLUMNS_TO_PRESERVE_ENTRY_COORDINATES)
# Input file selection
get_csv_file_selection_button(window, CSV_FILE_SELECTION_BUTTON_LABEL, ui_fonts, CSV_FILE_SELECTION_BUTTON_COORDINATES)
get_csv_file_selection_label(window, input_file, ui_fonts, CSV_FILE_SELECTION_LABEL_COORDINATES)
# CSV data scrambler
get_data_scrambler_button(window, DATA_SCRAMBLER_BUTTON_LABEL, columns_to_preserve_entry, ui_fonts, DATA_SCRAMBLER_BUTTON_COORDINATES)

## Hold until quit
window.mainloop()
