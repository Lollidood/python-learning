# Задача: посчитать стоимость выбранных ингредиентов бургера с использование ChainMap + Counter
# https://github.com/python-generation/Professional/tree/main/Module_6/Module_6.9/Module_6.9.23

from collections import ChainMap
from collections import Counter

# Словари с ценами на ингредиенты
bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

# Объединяем все словари в один (для удобного поиска цены по ингредиенту)
burger = ChainMap(bread, meat, sauce, vegetables, toppings)

# Ввод ингредиентов пользователем (через запятую)
ingr = input().split(',')

# Считаем, сколько раз каждый ингредиент встречается
count = Counter(ingr)

# Максимальная длина названия ингредиента (для выравнивания вывода)
maxi = max(map(len, ingr))

# Переменные для итоговой суммы и ширины таблицы
total_price = 0
line_len = 0

# Выводим ингредиенты в алфавитном порядке и считаем стоимость
for item in sorted(count):
    line = f'{item:<{maxi}} x {count[item]}'
    total_price += burger[item] * count[item]

    # Вычисляем максимальную ширину строки для оформления
    if len(line) > line_len:
        line_len = len(line)

    print(line)

# Итоговая строка
result_line = f'ИТОГ: {total_price}р'

