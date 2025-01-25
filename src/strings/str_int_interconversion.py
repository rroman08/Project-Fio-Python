
import functools
import string


def int_to_str(x: int) -> str:
    is_negative = False
    if x < 0:
        x, is_negative = -x, True

    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break
    # Adds the negative sign back if is_negative
    return ('-' if is_negative else '') + ''.join(reversed(s))


def str_to_int_long(s: str) -> int:
    result = 0
    for i in range(len(s)):
        if s[i] == '-':
            continue
        digit = string.digits.index(s[i])
        result = result * 10 + digit
    return -result if s[0] == '-' else result


def str_to_int(s: str) -> int:
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)  # Note that s[0] == '-' is a bool