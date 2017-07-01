prime = 3


def Search(text, pattern):
    patternl = len(pattern)
    textl = len(text)
    p = hashValue(pattern, patternl - 1)
    t = hashValue(text, patternl - 1)

    for i in range(1, textl - patternl + 2):
        if p == t:
            if compare2(text[i - 1:i + patternl - 1], pattern[0:]) is True:
                return i - 1;
        if i < textl - patternl + 1:
            t = rollIt(text, i - 1, i + patternl - 1, t, patternl)
    return -1;


def compare2(str1, str2):
    if len(str1) != len(str2):
        return False;
    i = 0
    j = 0
    for i, j in zip(str1, str2):
        if i != j:
            return False;
    return True


def hashValue(input, last):
    h = 0
    for i in range(last + 1):
        h = h + ord(input[i])*pow(prime, i)
    return h


def rollIt(input, oldIndex, newIndex, h, patternl):
    nh = h - ord(input[oldIndex])
    nh = nh / prime
    nh += ord(input[newIndex]) * pow(prime, patternl - 1)
    return nh;

position = Search("hehuhjhjhjbhbhyubhucodeplagio", "bhucodeplagio")
print("Index ", position)