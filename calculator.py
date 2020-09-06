import math

# Exercise 1
# 
# def add(x,y):
#    pass

# Exercise 2
# def add(x,y):
#    return x+y

# Exercise 3
# def add(x,y):
#     return x+y

# Exercise 4
def factorial(N):
    if N < 0:
        result = 0
    elif N == 0:
        result = 1
    else: 
        result = 1
        for i in range(1,N+1):
            result = result*i
    return result
            
def sin(x,N):
    result = 0
    for i in range(0,N+1):
        result = result + ((-1.0)**i)*(x)**(2*i+1)/factorial(2*i+1)
    return result

def divide(x,y):
    return x/y

def cos(x,N):
    result = 0
    for i in range(0,N+1):
        result = result + ((-1.0)**i)*(x)**(2*i)/factorial(2*i)
    return result

def exp(x,N):
    result = 0
    for i in range(0,N+1):
        result = result + ((x)**(i)/factorial(i))
    return result