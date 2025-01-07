from abc import ABC  
  
class Rbi(ABC):   
  
   # abstract method   
   def sides(self):   
      pass  
  
class Indian(Rbi):   
  
     
   def sides(self):   
      print("Rateof Int 7.5")   
  
class Icici(Rbi):   
  
     
   def sides(self):   
      print("Rateof Int 8.5")   
  
class Hdfc(Rbi):   
  
   def sides(self):   
      print("Rateof Int 9.5")   
  
class Axis(Rbi):   
  
   def sides(self):   
      print("Rateof Int 10.5")   
  
# Driver code   
t = Indian()   
t.sides()   
  
s = Icici()   
s.sides()   
  
p = Hdfc()   
p.sides()   
  
k = Axis()   
k.sides()   