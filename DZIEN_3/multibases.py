def logger(self,m,n):
    return f'{m}: {n}'

class MultiBases(type):
    def __new__(cls,classname,bases,attrs):
        if len(bases)>1:
            raise TypeError('dotępne jest tylko jednodziedziczenie!')
        return super().__new__(cls,classname,bases,attrs)

    def __init__(self,classname,bases,attrs):
        self.logger = logger

class Base(metaclass=MultiBases):
    pass

class A(Base):
    pass

class B(A):
    pass

class Ekstra:
    pass

# class Test(Ekstra,B):
#     pass

b = B()
print(f"{b.logger(23,'informacja')}")

def policz(self,x,y):
    return x-2*y

B.logger = policz

c = B()
print(c.logger(13,4))

class C(B):
    pass

ob = C()
print(ob.logger(2,1))
