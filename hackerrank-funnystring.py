def funnyString(s):
    # Write your code here
    a=s
    b=a[::-1]
    c=[]
    d=[]
    for i in range(0,len(a)):
        if i<3:
            c.append(ord(a[i+1])-ord(a[i]))
        else:
            c.append(ord(a[-1])-ord(a[i]))
    #print(c)
    for i in range(0,len(b)):
        if i<3:
            d.append(ord(b[i])-ord(b[i+1]))
        else:
            d.append(ord(b[-1])-ord(b[i]))
    #print(d)
    flag=0
    for i in range(len(c)):
        if c[i]==d[i]:
            flag=0
        else:
            flag=1
            break
    if flag==0:
        print("Funny")
    else:
        print("Not Funny")

s=input()
funnyString(s)