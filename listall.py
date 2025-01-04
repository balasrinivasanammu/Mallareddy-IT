# a simple list   
list1 = [1, 2, "Python", "Program", 15.9]      
  
# printing the list  
print(list1)  
  
# printing the type of list  
print(type(list1))  

#-------------------------------
'''
The characteristics of the List are as follows:

The lists are in order.
The list element can be accessed via the index.
The mutable type of List is
The rundowns are changeable sorts.
The number of various elements can be stored in a list.
'''
#--------------------
emp = [ "Mango City", 50, "Salem"]    
print("printing employee data ...")      
print(" Name : %s, ID: %d, Country: %s" %(emp[0], emp[1], emp[2]))


#------------------------------

list = [1,2,3,4,5,6,7]    
print(list[0])    
print(list[1])    
print(list[2])    
print(list[3])    
# Slicing the elements    
print(list[0:6])    
# By default, the index value is 0 so its starts from the 0th element and go for index -1.    
print(list[:])    
print(list[2:5])    
print(list[1:6:2])

print(list[-1])    
print(list[-3:])    
print(list[:-1])    
print(list[-3:-1])  


# updating list values  
list = [1, 2, 3, 4, 5, 6]       
print(list)       
# It will assign value to the value to the second index     
list[2] = 10     
print(list)      
# Adding multiple-element     
list[1:3] = [89, 78]       
print(list)     
# It will add value at the end of the list    
list[-1] = 25    
print(list)

#Python List Operations

'''
Repetition
Concatenation
Length
Iteration
Membership
'''

list1 = [12, 14, 16, 18, 20]  
# repetition operator *  
l = list1 * 2  
print(l)

list1 = [12, 14, 16, 18, 20]  
list2 = [9, 10, 32, 54, 86]  
# concatenation operator +  
l = list1 + list2  
print(l)

# declaring the list  
list1 = [12, 14, 16, 18, 20, 23, 27, 39, 40]  
# finding length of the list  
len(list1)

list1 = [12, 14, 16, 39, 40]  
# iterating  
for i in list1:   
    print(i)
    
list1 = [100, 200, 300, 400, 500]  
# true will be printed if value exists  
# and false if not  
  
print(600 in list1)  
print(700 in list1)  
print(1040 in list1)  