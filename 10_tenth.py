#scope 

def f1(n1):
    
    def f2(n2):
       return n1 ** n2
    return f2

result = f1(2)

print(result(3))