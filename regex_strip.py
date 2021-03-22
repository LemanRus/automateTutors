import re


def regex_strip(*strings):
    strip_start = re.compile(r"^\s*")
    strip_end = re.compile(r"\s*$")
    if len(strings) == 1:
        return strip_start.sub(st)
    else:
        return strip_end.sub(strings[1], strings[0])


print(regex_strip(" jlkhjlkh "))
print(regex_strip(" ggjhgjhghg ", "SPAM"))