# creating a dictionary
per_info = {
  "name": "Balaji", 
  "age": 50, 
  "native": "mango city"
}

# printing the dictionary
print(per_info)
print(per_info["age"])

per_info["salary"] = 75555.55
print(per_info)
per_info["salary"] = 85555.55
print(per_info)

#per_info.clear()

for temp in per_info:
    print(temp)

print()

# print dictionary values one by one
for temp1 in per_info:
    a = per_info[temp1]
    print(a)