import random
import time
import math
import fileinput


def file_reader(file):
    with open(file, 'r') as file:
        for line in file:
            yield line.strip()


def create_word_list(file):
    """Take the contents of `file` and format into 
    a useable list of words

    :param file: the unformatted file
    :type file: str
    """
    with fileinput.FileInput(file, inplace=True) as unformatted_file:
        for line in (line for line in unformatted_file):
            word = ''
            for char in line:
                if char.isalpha():
                    word += char
            if word:
                print(word)


def word_list_loader(file):
    """Creates a list of words based on contents of `file`

    :param file: the file path of words list
    :type file: str
    """
    word_list = []
    for word in file_reader(file):
        word_list.append(word)
    return word_list


def str_gen(word_list, words_num):
    """Generate words from `word_list` and add them to `word_str`,
    separated by commas. Return the new str

    :param word_list: the list of words to select from
    :type word_list: list
    :param word_str: the string words will be added to
    :type word_str: str
    :param words_num: the number of words that will be generated
    :type words_num: int
    """
    word_str = ''
    for i in range(words_num):
        word_index = math.trunc(random.random() * len(word_list))
        word_str += ' ' + word_list[word_index]
    return word_str.strip()


def word_counter(input_str):
    """Count words in `input_str` based on whitespaces. 
    Will only count a space if previous char was not a space 
    """
    # will not count last word if no whitespace at end
    counting_str = input_str.lstrip() + ' '
    total_words = 0
    previous_char = False
    for char in counting_str:
        if not char.isspace():
            previous_char = True
        elif previous_char:
            total_words += 1
            previous_char = False
    return total_words


def str_to_list(*input_str):
    return_list = []
    for x in input_str:
        return_list.append(x.split())
    return return_list


def word_checker(original_str, string_to_check):
    original_words, new_words = str_to_list(original_str, string_to_check)
    correct_words = 0

    for i in range(len(new_words)):
        try:
            if new_words[i] == original_words[i]:
                correct_words += 1
        except IndexError:
            break
    return correct_words


def run_test(words_num, words_list):
    original_str = str_gen(words_list, words_num)

    start_time = time.time()
    input_str = input(original_str + '\n\n')
    end_time = time.time()

    total_words = word_counter(input_str)
    correct_words = word_checker(original_str, input_str)
    time_taken = round(end_time - start_time)
    wpm = round((total_words / time_taken) * 60)
    correct_wpm = round((correct_words / time_taken) * 60)

    print("""Time Taken: {} seconds
    WPM: {}
    Total Words: {}
    Correct Words: {}
    Correct WPM: {}""".format(
        time_taken, wpm, total_words, correct_words, correct_wpm))


if __name__ == '__main__':
    print("Welcome to the Speed Test!")
    words_num = int(input("How Many Words? "))
    word_list = word_list_loader("./200_words.txt")
    run_test(words_num, word_list)
