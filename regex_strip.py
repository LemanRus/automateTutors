import re


def regex_strip(*strings):
    strip_start = re.compile(r"^\s*")
    strip_end = re.compile(r"\s*$")
    stripped_string = ""
    if len(strings) == 1:
        stripped_string = strip_start.sub("", strings[0])
        stripped_string = strip_end.sub("", stripped_string)
        return stripped_string
    else:
        stripped_string = strip_start.sub(strings[1], strings[0])
        stripped_string = strip_end.sub(strings[1], stripped_string)
        return stripped_string


print(regex_strip(" jlkhjlkh      "))
print(regex_strip("       ggjhgjhghg      ", "SPAM"))
