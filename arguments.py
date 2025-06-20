#positional arguments:-
def add(x,y):
    c=x+y
    print(c)
add(4,6)
#keyword arguments:-
def show(name,age):
    print(name,age)
show(name='kiran',age='25')
#default arguments:-
def show(name,age=27):
    print(name,age)
show(name='ram',age=62)
#variable length arguments
def display(*x):
    x=x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]
    print(x)
display(10,10,10,10,10,10,10)
#key variable length arguments
def add(**num):
    z=num['a']+num['b']+num['c']
    print(z)
add(a=1,b=2,c=3)
