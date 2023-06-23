def proc_calc_input_dict(input_list, op_definitions: dict):
    '''
    NOTE: NO LONGER IN USE

    Convert a list of inputs to dictionary of outputs.

    op_definitions should be formatted like this:
    {"+": operator.add} etc.

    Dictionary key = `position` `element` (eg: 0 12.4  or  1 +) as a single string
    Dictionary value = type (is it number or operator?) as a string 
    '''

    proc_input = {}  # store the processed input

    for i, element in enumerate(input_list):
        try:
            # convert `element` to float and add as a key to proc_input if `element` is a number
            # add index so there is a unique key for every element
            # add "number" as value for `element` in proc_input

            proc_input[f"{i} {float(element)}"] = "number"

        except:  # if not number
            print(f"{element} is not a number")  # TODO remove

            if element in op_definitions.keys():  # if is operator
                # append the associated function
                proc_input[f"{i} {op_definitions[element]}"] = "operator"
            else:
                raise Exception(f"Invalid Character {element}")

    return proc_input


def convert_to_list_old(proc_input: list):
    '''Place the input into indented lists ignoring bidmass,
    so each element is completed in order'''
    # TODO implement bidmas
    formatted_list = []  
    for pos, element in enumerate(proc_input):
        if pos <= 2:  # first 3 elements
            # add to first indented list (ignore bidmas)
            formatted_list.append(element)
        else:
            if type(element) == float:  # is number
                # numbers (unless at start) must be after an operator,
                # so we don't want to "break off" the existing list
                # this just appends to the end of the least indented list
                # like this: [[1+2]+] -> [[1+2]+3]
                formatted_list.append(element)
            else:  # must be an operator
                # wrap the existing expression in a list, then add the operator
                # to the least indented list
                # like this: [1+2] -> [[1+2]] -> {[1+2]+]
                formatted_list = [formatted_list]
                formatted_list.append(element)

        """ else:
            if pos % 2 != 0:  # is odd, so is operator
                # wrap the existing expression in a list, then add the operator
                # to the least indented list
                # like this: [1+2] -> [[1+2]] -> {[1+2]+]
                formatted_list = [formatted_list]
                formatted_list.append(element)
            else:
                # numbers (unless at start) must be after an operator,
                # so we don't want to "break off" the existing list
                # this just appends to the end of the least indented list
                # like this: [[1+2]+] -> [[1+2]+3]
                formatted_list.append(element) """

    return formatted_list