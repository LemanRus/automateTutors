tableData = [['яблоки', 'апельсины', 'вишни', 'бананы'],
['Алиса', 'Боб', 'Кэрол', 'Дэвид'],
['собаки', 'кошки', 'лось', 'гусь']]


def print_table(table):
    new_table = []
    for row in table:
        max_len = len(max(row, key=len)) + 1
        new_table.append([])
        for string in row:
            new_table[-1].append([string, max_len])

    trans_table = list(zip(*new_table))

    for row in trans_table:
        for inner in row:
            print(inner[0].rjust(inner[1]), end='')
        print()




print_table(tableData)