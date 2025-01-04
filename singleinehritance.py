# Parent Class 1
class A:
    def method(self):
        print("Method in class A")

# Parent Class 2
class B(A):
    def method(self):
        print("Method in class B")
        super().method()

# Child Class
class C(B):
    def method(self):
        print("Method in class C")
        super().method()

# Creating an object of class C
obj = C()
obj.method()
