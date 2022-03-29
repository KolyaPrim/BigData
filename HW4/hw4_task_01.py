

def read_magic_number(path: str) -> bool:
    with open(path) as file:
        result = True
        try:
            linenumber = file.readline().split()
            for i in range(0, len(linenumber)):
                if float(linenumber[i]) >= 1.0 and float(linenumber[i]) < 3.0:
                    pass
                else:
                    return False
        except ValueError:
            return ValueError

        return result


print(read_magic_number("src/file.txt"))
