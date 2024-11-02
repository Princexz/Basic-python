# A simple class in python with name and age as parameters
# input method takes the marks input and display method prints all the information
# self refers to the object for which it is called
# all methods need to be passed with self keyword

class simple:
    #constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.marks=[]           # list in python to store marks in various subjects
    #methods
    def marks_input(self): 
        for i in range(5):
            marks_subject=int(input("Marks for subject "+str(i+1)+":"))
            self.marks.append(marks_subject)
    def display_data(self):
        total=sum(self.marks)
        avg=total/len(self.marks)
        print("Name:",self.name)
        print("Age:",self.age)
        print("Total:",total)
        print("Average:",avg)

def main():
    # Creating an instance
    obj=simple("Mohit",21)
    obj.marks_input()
    obj.display_data()
    
                
    
main()
