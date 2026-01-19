from string import digits


def generate_emails(existing: list[str], new_users: list[str]) -> list[str]:
    """Генерирует уникальные email-адреса для новых пользователей.
    existing — список уже зарегистрированных email
    new_users — список логинов новых пользователей
    """
    logins = {}

    # Обрабатываем уже существующие email
    for email in existing:
        login = email.split('@')[0]
        base = login.rstrip(digits)      # логин без цифр в конце
        num = login[len(base):]          # цифры в конце (если есть)

        if num:
            logins.setdefault(base, []).append(int(num))
        else:
            logins.setdefault(base, []).append(0)

    result = []

    # Генерируем email для новых пользователей
    for login in new_users:
        if login not in logins:
            result.append(f"{login}@beegeek.bzz")
            logins.setdefault(login, []).append(0)
        else:
            i = 0
            while i in logins[login]:
                i += 1

            if i == 0:
                result.append(f"{login}@beegeek.bzz")
            else:
                result.append(f"{login}{i}@beegeek.bzz")

            logins[login].append(i)

    return result
