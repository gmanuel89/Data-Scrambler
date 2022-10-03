## Import libraries and functions
import pandas as pd

## Read input file as dataframe
def read_data_frame(input_file: str | list[dict]) -> pd.DataFrame:
    # Initialise output
    input_data_frame = None
    # File path
    if isinstance(input_file, str):
        # CSV
        if str(input_file).lower().endswith('.csv'):
            input_data_frame = pd.read_csv(input_file)
        elif str(input_file).lower().endswith('.xlsx') or str(input_file).lower().endswith('.xls'):
            input_data_frame = pd.read_excel(input_file)
        else:
            pass
    elif isinstance(input_file, list):
        if len(input_file) > 0 and isinstance(input_file[0], dict):
            input_data_frame = pd.DataFrame.from_dict(input_file)
    else:
        pass
    # return
    return input_data_frame