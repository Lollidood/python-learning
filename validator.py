import pytest
from string import digits


def is_good_password(text: str) -> bool:
    """Checks whether a password is strong.
    Requirements:
    - length at least 9 characters
    - at least one uppercase letter
    - at least one lowercase letter
    - at least one digit"""

    if not isinstance(text, str):
        raise TypeError("Password must be a string")

    return (
        len(text) >= 9
        and any(i.isupper() for i in text)
        and any(i.islower() for i in text)
        and any(i.isdigit() for i in text)
    )
