
def is_palindromic(s: str) -> bool:
    # Note that s[~i] for i in [0, 1, 2] is s[-(i+1)]
    return all(s[i] == s[~i] for i in range(len(s) // 2))


def is_palindromic_pythonic(s: str) -> bool:
    return s == s[::-1]


def is_palindromic_long(s: str) -> bool:
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True


if __name__ == '__main__':
    print(is_palindromic('malayalam'))
    print(is_palindromic_pythonic('malayalam'))
    print(is_palindromic_long('malayalam'))
