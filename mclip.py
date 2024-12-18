# !Python3
# Программа с несколькими буферами обмена

TEXT = {"да"  : "Согласен", "нет" : "Не согласен", "хз" : "Я подумаю"}

import sys, pyperclip
if len(pyperclip.paste()) < 1:
    print(" Пустой буфер обмена")
    sys.exit()
if pyperclip.paste() in TEXT:
    print("Текст для ***" + pyperclip.paste() + "*** скопирован в буфер обмена")
    pyperclip.copy(TEXT[pyperclip.paste()])
else:
    print("Значения для ***" + pyperclip.paste() + "*** нет в словаре")
    sys.exit()
