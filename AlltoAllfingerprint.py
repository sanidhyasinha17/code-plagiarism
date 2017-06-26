import string
def stepone(str):
    list3=[]
    str= str.translate(string.maketrans("",""), string.whitespace)
    str= str.translate(string.maketrans("",""), string.punctuation)
    for t in range(len(str)-9+1):
            list3.append(str[t:t+9])
    return list3

def steptwo(list3):
    list2=[]
    j=len(list3)
    list1=[]
    for i in range(j):
        h=0
        for k in range(9):
            h = h + ord(list3[i][k]) * pow(2, 9-k-1)
        list1.append(h)
    print list1
    
    for l in range(j):
        if (list1[l]%4==0):
            list2.append(list1[l])
    return list2

str="fsha aegfaefg srths rtyarhy arha rklhnsg.a.vld;l,hf sfhz s6tnysu4 56a46ub8"
x=stepone(str)
print x
s=steptwo(x)
print s
