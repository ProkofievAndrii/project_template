import pandas as pd


def input_text_from_console():
    """
    Function to input text from the console.

    Returns:
        str: Text input by the user.
    """
    text = input("Input text: ")
    return text


def read_text_from_file_builtin(file_path):
    """
    Function to read text from a file using built-in capabilities.

    Args:
        file_path (str): The path to the file from which text will be read.

    Returns:
        str: Text read from the file.
            Returns "Error: File not found" if the file is not found.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        return "Error: File not found"


def read_text_from_file_with_pandas(file_path):
    """
    Function to read text from a file using the pandas library.

    Args:
        file_path (str): The path to the file from which text will be read.

    Returns:
        str: Text read from the file.
            Returns "Error: File not found" if the file is not found.
    """
    try:
        data = pd.read_csv(file_path)
        text = data.iloc[:, 0].name
        return text
    except FileNotFoundError:
        return "Error: File not found"
