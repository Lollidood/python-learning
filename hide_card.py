def hide_card(card):
"""
Hides a card number, leaving only the last 4 digits.
All other digits are replaced with '*'.
"""
   
    digits = ''.join(ch for ch in card if ch.isdigit())

    # if there are fewer than 4 digits, return as is
    if len(digits) < 4:
        return digits

    # form the result
    return '*' * (len(digits) - 4) + digits[-4:]
