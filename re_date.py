import re

date = re.compile(r"(0?[1-9]|[12]\d|30|31)/(0?[1-9]|1[0-2])/(\d{4}|\d{2})")

print(date.fullmatch("12/30/1985").group(0))
print(date.fullmatch("2/30/1985").group(0))
print(date.fullmatch("02/04/1985").group(0))
print(date.fullmatch("2/4/85").group(0))