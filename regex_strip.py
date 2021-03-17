import re


def regex_strip(*strings):
    strip_pattern = re.compile(r"^(\s)(.*)(\s)$")
    if len(strings) == 1:
        return strip_pattern.sub(r"\1\2", strings[0])
    else:
        return strip_pattern.sub(strings[1], strings[0])


print(regex_strip(" jlkhjlkh "))
print(regex_strip(" ggjhgjhghg ", "SPAM"))