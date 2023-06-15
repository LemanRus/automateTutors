#! python3
# mcb.pyw - сохраняет и загружает фрагменты текста в буфер обмена
#
# Использование: py.exe mcb.pyw save <ключевое_слово> - сохраняет содержимое
#                   буфера обмена с ключевым словом
#                py.exe mcb.pyw <ключевое_слово> - загружает текст, соответствующий ключевому слову,
#                    в буфер обмена
#                py.exe mcb.pyw list - загружает все ключевые слова в буфер обмена

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    pass # TODO: сформировать список ключевых слов и загрузить содержимое

mcb_shelf.close()
