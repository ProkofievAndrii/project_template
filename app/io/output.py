def print_text_to_console(text):
    """
    Function to print text to the console.

    Args:
        text (str): The text to be printed to the console.
    """
    print(text)


def write_text_to_file(file_path, text):
    """
    Function to write text to a file.

    Args:
        file_path (str): The path to the file where text will be written.
        text (str): The text to be written to the file.

    Returns:
        str: Error message if file not found.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(text)
    except FileNotFoundError:
        return "Error: File not found"


def append_text_to_file(file_path, text):
    """
    Function to append text to a file.

    Args:
        file_path (str): The path to the file where text will be appended.
        text (str): The text to be appended to the file.

    Returns:
        str: Error message if file not found.
    """
    try:
        with open(file_path, 'a') as file:
            file.write(text)
    except FileNotFoundError:
        return "Error: File not found"
