import string
def stepone(str):
    list3=[]
    str= str.translate(string.maketrans("",""), string.whitespace)
    str= str.translate(string.maketrans("",""), string.punctuation)
    v=(len(str)/9)*9
    for t in range(v):
            list3.append(str[t:t+ 9])
    return list3
def steptwo(list):
    list2=[]
    j=len(list)
    list1=[]
    for i in range(j):
        h=0
        for k in range(9):
            h = h + ord(list[i][k]) * pow(3, k)
        list1.append(h)
        list1.sort()
    return list1[0:4]
str="fsha aegfaefg srths rtyarhy arha rklhnsg.a.vld;l,hf sfhz s6tnysu4 56a46ub8"
x=stepone(str)
print x
s=steptwo(x)
print s
