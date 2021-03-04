table_data = [["apples", "oranges", "cherries", "banana"],
              ["Alice", "Bob", "Carol", "David"],
              ["dogs", "cats", "moose", "goose"]]


def print_table(table):
    col_width = [0] * len(table)
    for i in range(len(table_data)):
        col_width[i] = max(len(element) for element in table_data[i])

    adjust = max(col_width)
    for i in range(len(table_data[0])):
        for j in range(len(table_data)):
            print(table_data[j][i].rjust(adjust + 1), end="")
        print()


print_table(table_data)
