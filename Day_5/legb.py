#rules of legb

x="global"

def outer():
    x="enclosing"
    def inner():
        x="local"
        print("Inner: ",x)
    inner()
    print("outer: ",x)

outer()
print("global: ", x)    
