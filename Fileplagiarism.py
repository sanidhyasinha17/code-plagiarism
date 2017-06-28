import string
def stepone(str):
    list3=[]
    str= str.translate(string.maketrans("",""), string.whitespace)
    str= str.translate(string.maketrans("",""), string.punctuation)
    for t in range(len(str)-8):
            list3.append(str[t:t+ 9])
    return list3
def steptwo(list):
    list2=[]
    j=len(list)
    list1=[]
    for i in range(j):
        h=0
        for k in range(9):
            h = h + ord(list[i][k]) * pow(3,9-k-1)
        list1.append(h)
        list1.sort()
    return list1[0:4]

fol = open("hitachi.txt",'r')
str2=fol.read()
fol.close()
fo = open("azure.txt",'r')
str1=fo.read()
fo.close()
l5=stepone(str1)
l5=steptwo(l5)
l6=stepone(str2)
l6=steptwo(l6)
if (l5==l6):
    print "matching"
else:
    print "not matchingg"