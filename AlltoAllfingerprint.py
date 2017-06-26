import string
def stepone(str):
    list3=[]
    str= str.translate(string.maketrans("",""), string.whitespace)
    str= str.translate(string.maketrans("",""), string.punctuation)
    for t in range(len(str)/9):
            list3.append(str[t * 9:(t * 9) + 9])
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
    for l in range(j):
        if (list1[l]%4==0):
            list2.append(list1[l])
    return list2
str="fsha aegfaefg srths rtyarhy arha rklhnsg.a.vld;l,hf sfhz s6tnysu4 56a46ub8"
x=stepone(str)
print x
s=steptwo(x)
print s
