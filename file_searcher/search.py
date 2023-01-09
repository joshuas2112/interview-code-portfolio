def positive(num: int) -> int:
    """
    Turns a negative number into the "matching" positive one. 
    """
    if num < 0:
        num -= num * 2
    return num


def posintinator(input_str: str = 0) -> int:
    """
    Turn a value into an int

    Round floats to integers, return 0 if `input_str` is not an int or 
    float

    Return 0 if nothing is entered

    :param input_str: [description], defaults to 0
    :return: The closest int to the number entered, 0 if not a number
    """
    try:    # find if it's an int already
        return_int = int(input_str)
    except:
        try:    # check if it's a float
            return_int = round(float(input_str))    # round to an int
            print("Rounding Value to: {}".format(return_int))
        except Exception:     # return 0 if all else fails
            print("String Not Valid - Returning 0")
            return_int = 0
    return abs(return_int)


def main():
    # get search criteria
    file = input("Please enter a file path to search: ")
    search_term = input("Please enter a search term: ").casefold()
    output_length = posintinator(input(
        "Please enter a maximum length for output following result (default = 0): "))
    show_fail = input("Would you like to see failures? [Y/n] ").casefold()

    try:    # check if file path is valid
        test_path = open(file, 'r')
        test_path.close()
        correct_path = file
    except:     # default to search_file.txt
        correct_path = "./search_file.txt"
        print(f"Invalid Path, defaulting to '{correct_path}'\n")

    with open(correct_path, 'r') as searching_file:
        if search_term != "":   # code breaks if search_term empty
            # show the user search criteria
            print(f"Searching for '{search_term}' in '{correct_path}'\n")

            for line_num, line in enumerate(searching_file):
                if search_term in line.casefold():
                    for char_i in range(len(line)):
                        # check if the current character and those after match search
                        if (line[char_i:char_i+len(search_term)]
                                .casefold()) == search_term:
                            # print matching characters and `output_length` more
                            print(line[char_i:char_i+len(search_term)+output_length]
                                  .rstrip("\n"))
                elif show_fail != "n":
                    print(f"not in line {line_num+1}")
        else:
            for line in searching_file:
                print(line, end="")


if __name__ == '__main__':
    main()
