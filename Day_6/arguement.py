#nested function
def outer (x):
    def inner(y):
        return x+y
    return inner

add_five=outer(5)
result=add_five(6)
print(add_five)
print("Final result is: ", result)

#pass function arguement

def add(x,y):
    return x+y
def mul(x,y):
    return "multiplication is ",x*y
def calculate(func,x,y):
    return func(x,y)

result=calculate(add,8,20)
res=calculate(mul,4,5)
print("addition is ", result)
print(res)

def fabonacci():
    a,b=0,1
    while True:
        yield a
        
         
