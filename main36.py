class a:
    def __init__(self):
        print("hi")
    def __del__(self):
        print("I have deleted the object")
    
def func1():
    obj=a()
    print("function end")
    return func1

callfunc1=func1()
l=["Banana","apple","kiwi"]
print(list(enumerate(l)))
    
    