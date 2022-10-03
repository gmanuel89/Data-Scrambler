## Import libraries and functions
import pandas as pd
import random

from pyparsing import col

## Scramble data content from file
def scramble_file_data_content(input_data_frame: pd.DataFrame, columns_to_preserve: list[str]) -> pd.DataFrame:
    # Initialise output
    input_data_frame_scrambled = input_data_frame
    # Determine column types
    column_types = input_data_frame.dtypes
    # Step 1: shuffle rows (keep the row structure intact)
    input_data_frame_scrambled = input_data_frame.sample(frac=1).reset_index()
    # Step 2: multiply numbers by a factor between 0.1 and 2
    for colname, values in input_data_frame_scrambled.iteritems():
        if colname in column_types and not colname in columns_to_preserve:
            if column_types[colname] == 'float64' or column_types[colname] == 'int64':
                for v in input_data_frame_scrambled[colname]:
                    random_number = random.uniform(0.1, 2.0)
                    input_data_frame_scrambled[colname] = input_data_frame_scrambled[colname].replace(v, v * random_number)
    # return 
    return input_data_frame_scrambled
