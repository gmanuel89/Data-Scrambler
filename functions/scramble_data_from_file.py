## Import libraries
from functions.read_csv_file import read_csv_file
from functions.read_workbook import read_workbook
from functions.install_required_packages import install_required_packages
from functions.read_data_frame import read_data_frame
from functions.scramble_file_data_content import scramble_file_data_content

## Function to open the original CSV file and scramble the data from it
def scramble_data_from_file(input_file: str, columns_to_preserve: list[str]) -> list[dict]:
    # Initialise output
    input_data_frame_scrambled_output = []
    """
    # Determine if it is CSV or XSLX
    if str(input_file).lower().endswith('.xlsx') or str(input_file).lower().endswith('.xls'):
        install_required_packages(['openpyxl'])
        # Open the file
        input_csv_file_lines = read_workbook(input_file, None, output_format='dictionary')
    elif str(input_file).lower().endswith('.csv'):
        # Open the file
        input_csv_file_lines = read_csv_file(input_file, output_format='dictionary')
    else:
        return
    """
    # Read input file as data frame
    input_data_frame = read_data_frame(input_file)
    # Scramble data content
    input_data_frame_scrambled = scramble_file_data_content(input_data_frame, columns_to_preserve)
    # Return to csv format (python dictionary) (remove the pandas 'index' entry)
    input_data_frame_scrambled_output = input_data_frame_scrambled.to_dict(orient='records')
    for dfout in input_data_frame_scrambled_output:
        dfout.pop('index')
    # return
    return input_data_frame_scrambled_output
    