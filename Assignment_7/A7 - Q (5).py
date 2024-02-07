# Write a Python program to understand the use of
# global and nonlocal variables declared ina function.

g = "I am a global variable"
def outer():
    o = "I am an outer variable"
    def inner():
        nonlocal o
        global g
        o = "Modified outer variable"
        g = "Modified global variable"
        print("Inner - Outer Variable:", o)
        print("Inner - Global Variable:", g)
    inner()
    print("Outer - Outer Variable:", o)
    print("Outer - Global Variable:", g)
outer()
print("Outside - Global Variable:", g)