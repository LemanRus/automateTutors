def magic(lst):
    new_lst = []
    for i in lst:
        if i % 2:
            new_lst.append(i)
    return new_lst

if __name__ == '__main__':
    test = [[57, 12, 34, 67, 23, 97]]
    for sub_test in test:
        print('{}'.format(magic(sub_test)))