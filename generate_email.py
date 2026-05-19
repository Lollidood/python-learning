from string import digits

def generate_emails(existing: list[str], new_users: list[str]) -> list[str]:
    """Generates unique email addresses for new users.
    existing — list of already registered emails
    new_users — list of new user logins
    """
    logins = {}

    # Process existing emails
    for email in existing:
        login = email.split('@')[0]
        base = login.rstrip(digits)      # login without trailing digits
        num = login[len(base):]          # trailing digits (if any)

        if num:
            logins.setdefault(base, []).append(int(num))
        else:
            logins.setdefault(base, []).append(0)

    result = []

    # Generate emails for new users
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
