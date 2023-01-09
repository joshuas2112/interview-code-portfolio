with open("search_file.txt", 'r') as testing:
    new_line = ""
    for line in testing:
        new_line += line.rstrip("\n")

print(new_line)
