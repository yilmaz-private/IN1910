import calculator
import math

# Exercise 1
# def test_add():
#    a = 1
#    assert a == 1

# Exercise 2
# def test_add():
#    computed = calculator.add(0.1,0.2)
#    expected = 0.3
#    epsilon = 1e-08
#    assert abs(computed-expected) <= epsilon

# Exercise 3
# def test_add():
#     computed = calculator.add("Hello ", "World")
#     expected = "Hello World"
#     assert computed == expected

# Exercise 4
def test_factorial():
    computed = calculator.factorial(9)
    expected = 362880
    assert computed == expected

def test_sin():
    computed = calculator.sin(3.14159265359,40)
    expected = 0
    epsilon = 1e-08
    assert abs(computed-expected) <= epsilon
    
def test_divide():
    computed = calculator.divide(2,4)
    expected = 0.5
    epsilon = 1e-08
    assert abs(computed-expected) <= epsilon

def test_cos():
    computed = calculator.cos(3.14159265359,40)
    expected = -1
    epsilon = 1e-08
    assert abs(computed-expected) <= epsilon

def test_exp():
    computed = calculator.exp(1,40)
    expected = 2.71828182845
    epsilon = 1e-08
    assert abs(computed-expected) <= epsilon