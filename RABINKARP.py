d=256
def Search(skepText, pattern, q):
    skepTextl = len(skepText)
    patternl = len(pattern)
    h = pow(d,patternl-1)%q
    p = 0
    t = 0
    result = []
    for i in range(patternl):
        p = (d*p+ord(pattern[i]))%q
        t = (d*t+ord(skepText[i]))%q
    for s in range(skepTextl-patternl+1):
        if p == t:
            test = True
            for i in range(patternl):
                if pattern[i] != skepText[s+i]:
                    test = False
                    break
            if test:
                result = result + [s]
        if s < skepTextl-patternl:
            t = (t-h*ord(skepText[s]))%q
            t = (t*d+ord(skepText[s+patternl]))%q
            t = (t+q)%q
    return result
print (Search("coecodcodeplagdkksdksksk", "codeplag", 11))
