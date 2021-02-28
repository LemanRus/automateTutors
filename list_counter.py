def list_counter(list):
    str = ""
    for i in range(len(list)-1):
        str += list[i] + ", "
    str += "and " + list[len(list)-1]
    return str