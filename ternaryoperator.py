a,b,c=10,20,30
res=a if a>b and a>c else b if b>c else c
print(res)
a,b,c,d = 10,20,30,40
res= a if a>b and a>c and a>d else b if b>c and b>d else c if c>d else d
print(res)