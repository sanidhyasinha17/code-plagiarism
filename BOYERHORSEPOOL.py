
def BoyerMooreHorspool(pattern, skepText):
    patternl = len(pattern)
    skepTextl = len(skepText)
    if patternl > skepTextl: return -1
    skip = []
    for i in range(256): skip.append(patternl)
    for i in range(patternl - 1): skip[ord(pattern[i])] = patternl - i - 1
    skip = tuple(skip)
    i = patternl - 1
    while i < skepTextl:
        j = patternl - 1; k = i
        while j >= 0 and skepText[k] == pattern[j]:
            j -= 1; k -= 1
        if j == -1: return k + 1
        i += skip[ord(skepText[i])]
    return -1

if __name__ == '__main__':
    skepText = "gugyugygyugiygcodeplag"
    pattern = "codeplag"
    ind = BoyerMooreHorspool(pattern, skepText)
    print (skepText)
    print (pattern)
    if ind > -1:
        print (ind)
