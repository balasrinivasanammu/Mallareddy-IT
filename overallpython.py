emp = ["balaji", "bytexl", "infosys", "kiwi", "mango"]
newlist = []

for x in emp:
  if "b" in x:
    newlist.append(x)

print(newlist)




#newlist = [expression for item in iterable if condition == True]

emp = ["balaji", "bytexl", "infosys", "kiwi", "mango"]

newlist = [x for x in emp if "b" in x]

print(newlist)


numbers = [1, 2, 3, 4]

dd_numbers = [num * 2 for num in numbers]

print(dd_numbers)

#----------------------

n = 51
res = "Even" if n % 2 == 0 else "Odd"
print(res)

#---------------------

n = -51

res = "Positive" if n > 0 else "Negative" if n < 0 else "Zero"
print(res)

#--------------------
#Ter opr using t

n = 7
res = ("Odd", "Even")[n % 2 == 0]

#--------------------
#Ter opr using d

a = 10
b = 20
max = {True: a, False: b}[a > b]
print(max)
print(res)