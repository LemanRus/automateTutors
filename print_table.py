table_data = [["apples", "oranges", "cherries", "banana"],
              ["Alice", "Bob", "Carol", "David"],
              ["dogs", "cats", "moose", "goose"]]


def print_table(table):
    col_width = [0] * len(table)
    for i in range(len(table_data)):
        col_width[i] = max(len(table_data[i]))

    print(col_width)


print_table(table_data)
