## Import libraries and functions
import pandas as pd

## Scramble data content from file
def scramble_file_data_content(input_data_frame: pd.DataFrame) -> pd.DataFrame:
    # Initialise output
    input_data_frame_scrambled = input_data_frame
    # Determine column types
    column_types = input_data_frame.dtypes
    # Step 1: shuffle rows (keep the row structure intact)
    input_data_frame_scrambled = input_data_frame.sample(frac=1).reset_index()
    # return 
    return input_data_frame_scrambled
