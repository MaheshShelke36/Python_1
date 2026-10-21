# using global
x="global"

def change_global():
    global x
    x="modified by global"
change_global()
print(x)    