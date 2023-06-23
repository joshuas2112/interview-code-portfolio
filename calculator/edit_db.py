import sqlite3


def insert_op(symbol, op, level):
    con = sqlite3.connect("operations.db")
    cur = con.cursor()
    insert_statement = f"""INSERT INTO Operations VALUES ('{symbol}', '{op}', {level})"""
    cur.execute(insert_statement)
    con.commit()
    con.close()


def all_ops():
    con = sqlite3.connect("operations.db")
    cur = con.cursor()
    for row in cur.execute(f"SELECT * FROM Operations"):
       print(row)
    con.close()


def main():
    # op_definitions_2 = {}

    # for key in op_definitions_2.keys():
    #     symbol = key
    #     op = op_definitions_2[key][0]
    #     level = op_definitions_2[key][1]
    #     insert_op(symbol, op, level)

    insert_op()
    all_ops()


if __name__ == '__main__':
    main()
