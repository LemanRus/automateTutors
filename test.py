def fun01(my_args):
    for name, value in enumerate(my_args):
        print('{0} is an {1}'.format(name, value))


def fun02(*my_args):
    for name, value in enumerate(my_args):
        print('{0} is an {1}'.format(name, value))


def fun03(**my_args):
    for name, value in enumerate(my_args):
        print('{0} is an {1}'.format(name, value))


fun02('abcd', 125, 88.33, [1, 22])  # b
