from app.io.input import input_text_from_console, read_text_from_file_builtin, read_text_from_file_with_pandas
from app.io.output import print_text_to_console, write_text_to_file, append_text_to_file


def main():
    text_from_console = input_text_from_console()
    print("Console input:", text_from_console)

    txt_input = "app/resources/input.txt"
    csv_input = "app/resources/input.csv"
    file_text_using_builtin = read_text_from_file_builtin(txt_input)
    file_text_using_pandas = read_text_from_file_with_pandas(csv_input)

    print("Text from file (built-in):", file_text_using_builtin)
    print("Text from file (pandas):", file_text_using_pandas)

    text = "TESTTESTTESTTESTTESTTESTTEST"

    print_text_to_console(text)

    txt_output = "app/resources/output.txt"

    write_text_to_file(txt_output, text)
    append_text_to_file(txt_output, "\nTESTTESTTEST")


if __name__ == "__main__":
    main()
