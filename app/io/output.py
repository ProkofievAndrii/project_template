def print_text_to_console(text):
    print(text)


def write_text_to_file(file_path, text):
    try:
        with open(file_path, 'w') as file:
            file.write(text)
    except FileNotFoundError:
        return "Error: File not found"


def append_text_to_file(file_path, text):
    try:
        with open(file_path, 'a') as file:
            file.write(text)
    except FileNotFoundError:
        return "Error: File not found"
