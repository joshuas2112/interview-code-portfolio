import math
import operator
import operations
import sqlite3
import readline


def proc_calc_input(input_list: list, op_definitions: dict):
    '''
    Convert any numbers in `input_list` to floats
    Return the processed list

    op_definitions should be formatted like this:
    {"+": operator.add} etc.
    '''

    # code could just go through and change any numbers in the original list
    # but this method allows us to raise and exception if there is an invalid character

    proc_input = []

    for element in input_list:
        try:
            # convert element to float and add to list
            proc_input.append(float(element))

        except:  # not a number
            if element.casefold() in op_definitions.keys():  # is operator
                proc_input.append(op_definitions[element.casefold()])
            else:  # is not a valid operator
                raise Exception(f"Invalid Character {element}")

    return proc_input


def convert_to_lists(proc_input: list, operations_db_path="operations.db", operations_db_table="Operations"):
    '''
    Sort the input into indented lists according to bidmas,
    so each element can be completed in order
    '''
    formatted_list = proc_input
    for i in range(0, 4):  # levels of bidmas
        # get all ops at the current level in a list
        # sqlite output is like [(func1,),(func2,)] etc
        curr_ops = [eval(op[0]) for op in search_ops(
            operations_db_path, operations_db_table, f'level = {i}', 'operation')]
        if not curr_ops:
            continue

        pos = 0
        while True:  # can't iterate over list itself because it shrinks
            try:
                element = formatted_list[pos]
            except:
                # When all elements in the list are nested, then break (fully sorted)
                break
            if element in curr_ops:  # is operator at current bidmas level
                prev_num = formatted_list[pos-1]
                next_num = formatted_list[pos+1]
                # indented list in position of the operator
                formatted_list[pos] = [prev_num, element, next_num]

                # remove the values that are now indented
                del formatted_list[pos+1]
                del formatted_list[pos-1]
                # don't increment pos because all elements have moved one down
            else: # is number
                pos += 1
    return formatted_list


def calc_in_order(expression: list):
    '''
    Use recursion to calculate a result from the innermost bracket (list)

    Uses the calculate() function to calculate results
    '''
    op = None  # used in rare case there is no op in expression, see bottom of this func
    current_numbers = []
    for element in expression:
        if type(element) == list:
            # use recursion to solve this indented list, it will keep going until it solves,
            # then work its way back
            current_numbers.append(calc_in_order(element))
        else:  # is a single number or operator
            if type(element) == float:  # is a number
                current_numbers.append(element)
            else:
                op = element
    if op:
        result = calculate(op, current_numbers)
    else:
        # expression looked like this: [[1+2]], so there is no op after solving ([3])
        if len(current_numbers) == 1:
            return current_numbers[0]
        else:  # likely invalid input (eg 1 2)
            raise Exception(
                f"Got multiple numbers ({current_numbers}) but no operator")
    return result


def calculate(op: "function", numbers_list: list):
    '''Return the result of the calculation `op` using parameters in `numbers_list`'''
    return op(*numbers_list)


def welcome(welcome_file_path: str):
    '''Prints out the contents of the welcome file at `welcome_file_path`'''
    with open(welcome_file_path, 'r') as welcome_file:
        print(*[line for line in welcome_file])  # print out the file
        print()


def load_ops(database_path, table_name):
    '''
    Load the operations into memory, as a dict:
    eg {"+": operator.add} etc
    '''
    op_definitions = {}  # symbal: op_func

    con = sqlite3.connect(database_path)
    cur = con.cursor()
    for row in cur.execute(f"SELECT symbol, operation FROM {table_name};"):
        symbol, op = row
        op_definitions[symbol] = eval(op)  # convert str to func, add to dict
    con.close()

    return (op_definitions)


def search_ops(database_path, table_name, condition, value_to_find):
    '''Return value in column `value_to_find` where condition is true'''
    con = sqlite3.connect(database_path)
    cur = con.cursor()
    res = cur.execute(
        f"SELECT {value_to_find} FROM {table_name} WHERE {condition}")
    value = res.fetchall()
    con.close()

    return value


def main():
    db_path = "operations.db"
    db_table_name = "Operations"
    op_definitions = load_ops(db_path, db_table_name)

    welcome("welcome.txt")

    # while True:
    # TODO make work without spaces
    usr_input = input("> ").split()  # splits based on spaces!!
    proc_input = proc_calc_input(usr_input, op_definitions)

    # debug:
    # print(usr_input)
    # print(proc_input)

    calc_list = convert_to_lists(proc_input)

    # debug
    # print(calc_list)

    print(calc_in_order(calc_list))


if __name__ == '__main__':
    main()
