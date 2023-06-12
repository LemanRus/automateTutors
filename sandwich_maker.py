import pyinputplus as pyip

bread = pyip.inputMenu(choices=["Цельнозерновой", "Белый", "Ржаной"], prompt="Выберите тип хлеба:\n", numbered=True)

protein = pyip.inputMenu(choices=["Курица", "Индейка", "Ветчина", "Тофу"], prompt="Выберите белковый продукт:\n",
                         numbered=True)

cheese = pyip.inputYesNo(prompt="Добавить сыр?\n", yesVal="Да", noVal="Нет")

cheese_type = pyip.inputMenu(choices=["Чеддер", "Швейцарский", "Моцарелла"], prompt="Выберите сыр:\n",
                         numbered=True)

mayo = pyip.inputYesNo(prompt="Добавить майонез?\n", yesVal="Да", noVal="Нет")

mustard = pyip.inputYesNo(prompt="Добавить горчицу?\n", yesVal="Да", noVal="Нет")

salad = pyip.inputYesNo(prompt="Добавить салат?\n", yesVal="Да", noVal="Нет")

tomato = pyip.inputYesNo(prompt="Добавить помидор?\n", yesVal="Да", noVal="Нет")

qty = pyip.inputInt(prompt="Сколько сделать бутербродов? ", min=1)

bread_price = {'Цельнозерновой': 0.15, 'Белый': 0.1, 'Ржаной': 0.1}
protein_price = {'Курица': 0.35, 'Индейка': 0.5, 'Ветчина': 0.3, 'Тофу': 0.55}
cheese_price = {'Чеддер': 0.15, 'Швейцарский': 0.1, 'Моцарелла': 0.12}

price = 0
price += bread_price[bread]
price += protein_price[protein]
price += cheese_price[cheese_type]

for choice in [mayo, mustard, salad, tomato]:
    if choice:
        price += 0.1

price *= qty

print(f'Вы должны мне {round(price, 2)} баксов')
