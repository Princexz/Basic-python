# Built in Data structures in python

def main():
    L=[5,4,3,2,1] # List
    T=(6,7,8,9,10) # Tuple
    D={'a':'apple','b':'ball','c':'cat'} # Dictionary(key-value pairs)
    # to check datatypes using type command in python
    print(type(L))
    print(type(T))
    print(type(D))
    # Traversing these structures using 'in' keyword
    print("Traversing List")
    for i in L:
        print(i,end=" ")
    print()
    print("Traversing Tuple")
    for j in T:
        print(j,end=" ")
    print()
    print("Traversing Dictionary")
    for k in D:
        print("Key:",k,"Value:",D[k])
    print()
    # Built in functions
    print("Length:",len(L),"Sum:",sum(L)) #length of list and sum of all elements in it
    print("Sorted List",sorted(L))  #to sort the list
main()
    
