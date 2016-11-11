a = 1
def x():
    global a
    a+=1
x()
print(a)
def y():
    global a
    a += 1
y()
print(a)
