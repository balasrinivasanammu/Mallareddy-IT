'''my_list = ["Apples,", "Bananas,", "Oranges,", "Grapes,"]

# Remove the last comma from each string element in the list
my_list = [item.rstrip(',') for item in my_list]

print(my_list)  # Output: ['Apples', 'Bananas', 'Oranges', 'Grapes']


a=[]
for i in range(0,10):
    a.append(i)
print(a)
'''

for i in range(10,20):
    print(i,end="," if i<19 else ".")
    
