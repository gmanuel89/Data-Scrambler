## Import libraries
import tkinter

## Get number of output chunks from UI entry
def get_columns_to_preserve_from_entry(columns_to_preserve_entry: tkinter.Entry) -> list[str]:
    # Initialise output
    columns_to_preserve = []
    # Get the value from the entry
    columns_to_preserve_string = str(columns_to_preserve_entry.get())
    # Split by comma
    columns_to_preserve_string_split = columns_to_preserve_string.split(',')
    if len(columns_to_preserve_string_split) > 0:
        for col in columns_to_preserve_string_split:
          columns_to_preserve.append(col.strip())  
    return columns_to_preserve