import string
import runpy
def stepone(str):
    list3=[]
    str = str.translate(string.maketrans("", ""), string.whitespace)
    str = str.translate(string.maketrans("", ""), string.punctuation)

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
    for i in range(j-8):
        list2.append(list1[i:i+4])
    return list2
def stepthree(list):
    finall=[]
    d={}
    j=len(list)
    for i in range(j-8):
        min=list[i][0]
        for k in range(3):
            if list[i][k+1]<=min:
                min=list[i][k+1]
        if (d.has_key(min)):
            if (d[min][1]<(k+1)):
                d[min]=[[i],k+1]
            elif (d[min][1]==(k+1)):
                d[min][0].append(i)
        else:
            d[min]=[[i],k+1]
    for s in d:
        for t in range(len(d[s][0])):
            finall.append((s, d[s][0][t]))
    for r in range(len(finall)-1,0,-1):
        for v in range(r):
            if finall[v+1][1]<finall[v][1]:
                finall[v],finall[v+1]=finall[v+1],finall[v]
    return finall
fol = open("hitachi.txt",'r')
str2=fol.read()
fol.close()
fo = open("azure.txt",'r')
str1=fo.read()
fo.close()
l5=stepone(str1)
l5=steptwo(l5)
l5=stepthree(l5)
l6=stepone(str2)
l6=steptwo(l6)
l6=stepthree(l6)


