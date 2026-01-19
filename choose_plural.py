def choose_plural(n: str|int, *args:list[str]) -> str:
    """Возвращает строку: "<n> <правильная форма слова>"."""

    n = str(n)
    forms = list(args[0])

    # Проверяем исключение: 11-19
    if len(n) > 1 and n[-2] == '1':
        return n + ' ' + forms[2]

    # Правила склонения
    if n[-1] == '1':
        return n + ' ' + forms[0]
    elif n[-1] in '234':
        return n + ' ' + forms[1]
    else:
        return n + ' ' + forms[2]


def test_choose_plural_one():
    assert choose_plural(1, ("яблоко", "яблока", "яблок")) == "1 яблоко"


def test_choose_plural_two():
    assert choose_plural(2, ("яблоко", "яблока", "яблок")) == "2 яблока"


def test_choose_plural_five():
    assert choose_plural(5, ("яблоко", "яблока", "яблок")) == "5 яблок"


def test_choose_plural_eleven():
    assert choose_plural(11, ("яблоко", "яблока", "яблок")) == "11 яблок"
