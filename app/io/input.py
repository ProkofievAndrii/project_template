import pandas as pd


def input_text_from_console():
    text = input("Input text: ")
    return text


def read_text_from_file_builtin(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        return "Error: File not found"


def read_text_from_file_with_pandas(file_path):
    try:
        data = pd.read_csv(file_path)
        text = data.iloc[:, 0].name
        return text
    except FileNotFoundError:
        return "Error: File not found"
