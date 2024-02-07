# Write a Python program to understand the use 
# of double asterisk(*) character declared in a function.

def d_ast(**kwargs):
    for key, value  in kwargs.items():
        print(key,":",value)
d_ast(name="Akash", age=21, city="Kaliyaganj")