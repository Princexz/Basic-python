# A simple function in python
# add function takes 2 arguments a,b and returns the sum

def add(a,b):
    return a+b

def main():
    a=int(input("Enter 1st no:"))
    b=int(input("Enter 2nd no:"))
    c=add(a,b)
    print("Sum of",a,"and",b,"is",c)

main()
