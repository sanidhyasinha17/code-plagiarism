# Python program for KMP Algorithm
def KMPSearch(pattern, skepText):
    M = len(pattern)
    N = len(skepText)


    lps = [0] * M
    j = 0


    computeLPSArray(pattern, M, lps)

    i = 0
    while i < N:
        if pattern[j] == skepText[i]:
            i += 1
            j += 1

        if j == M:
            print (i-j)

            j = lps[j - 1]


        elif i < N and pattern[j] != skepText[i]:

            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def computeLPSArray(pattern, M, lps):
    len = 0  # length of the previous longest prefix suffix

    lps[0]
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pattern[i] == pattern[len]:
            len += 1
            lps[i] = len
            i += 1
        else:

            if len != 0:
                len = lps[len - 1]


            else:
                lps[i] = 0
                i += 1


skepText = "cocococodeplagcocododi"
pattern = "codeplag"

KMPSearch(pattern, skepText)
