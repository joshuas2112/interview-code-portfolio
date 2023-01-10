import pickle
import random
import operator


def pickled_score_reader(pickle_file):
  with open(pickle_file, 'rb') as score_pickle:
    try:
      # TODO: what happens if there are multiple dicts in pickle file
      player_scores = pickle.load(score_pickle)  # load scores into a dict
    except:  # pickle file is empty
      player_scores = {}  # create new scores dict
      print("~ created new scores list ~")
  return player_scores


def avg_score(scores_dict, player, round_to=2):
  return round((scores_dict[player]['score'] / scores_dict[player]['tests']),
               round_to)


def print_scores(scores_dict):
  print("\n~ Starting Scores ~\n")
  for player in scores_dict:
    score = scores_dict[player]['score']
    avg = avg_score(scores_dict, player)
    print(f"{player}:\n\tTotal Score: {score}\n\tAverage: {avg}")
  print()


def random_operator():
  # operators - tuple containing functions to add etc.
  operators = (operator.add, operator.sub, operator.mul, operator.truediv)
  # select random operator function from `operators` and return
  return random.choice(operators)


def format_op(operator_function, word_or_sign='sign'):
  """
  Convert `operator_function` into an easily readable word or symbol

  Args:
    operator_function: the function to be formatted. Should be in form operator.add (can be add, sub, mul, truediv)
    word_or_sign: what should be returned. Should be either 'word', 'sign', or 'both'

  Return:
    the word (eg 'add') if word_or_sign == 'word'
    the sign (eg '+') if word_or_sign == 'sign'
    a tuple containing word and sign (eg ('add', '+')) if word_or_sign == 'both'
  """
  # NOTE: str(operator_function).split() = ['<built-in', 'function', 'add>']
  op_str = (str(operator_function).split()[2]).strip('>')
  if word_or_sign == 'word':
    return op_str

  # use dict to convert operator names to their signs eg 'add' -> '+'
  operators_signs_dict = {'add': '+', 'sub': '-', 'mul': '*', 'truediv': '/'}
  try:
    op_sign = operators_signs_dict[op_str]
  except:  # op_str not in operators_signs
    raise Exception("operator_function not valid")

  if word_or_sign == 'both':
    return (op_str, op_sign)
  else:  # either word_or_sign == 'sign' or something else - default to sign
    return op_sign


def pickle_scores(pickle_file, scores_dict):
  with open(pickle_file, 'wb') as scores_pickle:
    pickle.dump(scores_dict, scores_pickle)
    print("\n ~ saved scores ~ \n")


def get_name(names_dict):
  input_message = "Enter name\n> "
  while True:
    name = input(input_message)

    if name == "scores()":
      print_scores(names_dict)
    else:
      break
  
  if name not in names_dict:  # new player - add to scores dict
    names_dict[name] = {'score': 0, 'tests': 0}

  return name


def challenge39(questions_num=10):  # TODO: convert to functions-based
  player_scores = pickled_score_reader("./assets/challenge39_scores.pickle")
  print_scores(player_scores)
  commands = ["exit()", "scores()"]

  while True:
    name = get_name(player_scores)  # get name

    score = 0
    for i in range(questions_num):
      num1 = random.randint(1, 12)  # random int between 1 and 12 (inclusive)
      num2 = random.randint(1, 12)
      chosen_op = random_operator()
      op_sign = format_op(chosen_op)

      # get answer
      while True:
        try:
          usr_ans = float(
            input(
              f"Question {i+1}:\n{num1} {op_sign} {num2} ~ TO 1 DECIMAL PLACE\nAnswer: "
            ))
          break
        except:
          # answer was not a number
          print(
            "Please enter your answer as a number, rounded to 1 decimal place")
          continue

      # correct answer
      result = round(chosen_op(num1, num2), 1)

      # check answer
      if usr_ans == result:
        print("~ Correct! ~")
        score += 1
      else:
        print("-- Incorrect :( --\n")

      print(f"Score: {score}\n")
    print(f"~ Final Score: {score} ~\n")

    # add score to player's overall score
    player_scores[name]['score'] += score
    # increment number of tests (for averages, etc.)
    player_scores[name]['tests'] += 1
    avg = avg_score(player_scores, name)

    # print player profile summary
    print(
      f"{name}'s Total Score: {player_scores[name]['score']}\nAverage Score: {avg}"
    )

    pickle_scores("./assets/challenge39_scores.pickle", player_scores)


def main():
  challenge39()


if __name__ == '__main__':
  main()
