#! python3
# mcb.pyw - сохраняет и загружает фрагменты текста в буфер обмена
#
# Использование: py.exe mcb.pyw save <ключевое_слово> - сохраняет содержимое
#                   буфера обмена с ключевым словом
#                py.exe mcb.pyw <ключевое_слово> - загружает текст, соответствующий ключевому слову,
#                    в буфер обмена
#                py.exe mcb.pyw list - загружает все ключевые слова в буфер обмена

import pyperclip
import shelve
import sys

mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        mcb_shelf.pop(sys.argv[2])
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcb_shelf.clear()
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()