def is_good_password(text: str) -> bool:
    """Проверяет, является ли пароль надежным.
    Условия:
    - длина не менее 9 символов
    - есть заглавная буква
    - есть строчная буква
    - есть цифра"""

    if not isinstance(text, str):
        raise TypeError("Пароль должен быть строкой")

    return (
        len(text) >= 9
        and any(i.isupper() for i in text)
        and any(i.islower() for i in text)
        and any(i.isdigit() for i in text)
    )

def test_good_password():
    assert is_good_password("Abcdefg12") is True


def test_short_password():
    assert is_good_password("Abc12") is False


def test_no_uppercase():
    assert is_good_password("abcdefg12") is False


def test_no_lowercase():
    assert is_good_password("ABCDEFG12") is False