PASSWORDS = {"email" : "rohflekwrflkerj", "blog" : "woifjlkewrjnglkwerjg", "luggage" : "12345"}

import sys, pyperclip

if len(sys.argv) < 2:
    print("Использование: python pw.py [имя учётной записи] - копирование пароля учётной записи")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Пароль для " + account + " скопирован в буфер.")
else:
    print("Учётная запись " + account + " отсутствует в списке.")