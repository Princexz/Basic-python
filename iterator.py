# Implementing iterators using python
# Iterators can be made in python by using iter() method which takes iterable as argument
# then iteration is possible over it

def main():
    x=range(3)   #range object
    print(type(x))
    # to convert iterable into iterator we use iter() method
    it=iter(x)
    # iterating through iterator
    print(next(it))
    print(next(it))
    print(next(it))
    
main()
    
