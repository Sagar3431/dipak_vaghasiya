""" 
What is used to check whether an object o is an instance of class A?
the isinstance function is used to check whether an object is an instance of a specific class or a tuple of classes.
ex. isinstance(object, classinfo)

"""
class A:
    def massage(self):
        print("A")

class B(A):
    def massage1(self):
        print("HELLO")

o1 = A()
o2 = B()


print(isinstance(o1.massage(), A))  
print(isinstance(o2.massage1(), A))
print(isinstance(o1.massage(), B)) 
print(isinstance(o2.massage1(), B))
