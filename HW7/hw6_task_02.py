def backspace_method(s: str):
    i = 0
    while i < len(s):
        if s[i] == '#':
            if i == 0:
                s = s[1:]
            else:
                s = s[:i - 1] + s[i + 1:]
                i = 0
        i += 1
    return s


def backspace_compare(first: str, second: str):
    new_first = backspace_method(first)
    new_second = backspace_method(second)
    if new_first == new_second:
        return f"Output: True\nExplanation: both s and t become '{new_first}'"
    else:
        return f"Output: False\nExplanation: s becomes '{new_first}' " \
               f"while t becomes '{new_second}'"

print(backspace_compare("ab#c","ad#c"))