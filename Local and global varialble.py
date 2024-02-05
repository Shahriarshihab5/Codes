a=30 #global scope/variable
b=50

def fn():
    a=100 #local scope/variable
    print(a)

print(a)#printing the value of global variable
fn()#printing the value of local variable
