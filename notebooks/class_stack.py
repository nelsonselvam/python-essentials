class Stack:
    
    def __init__(self):  # defining the constructor that will help to instantiate the object
        # adding a new property to the class is done by the constructor
        print("Intitiating the constructor")
        self.__stack_list = []  # names starting with '__' will make them private
        
    # self has to be passed mandatorily as the first parameter to all the methods in the calls
    # self is generally referred, but it can be anything that makes sense
    # 'this' also works
    def push(self,val):                 
        self.__stack_list.append(val)
        
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
    
    def __getitem__(self):
        return self.__stack_list

stack_obj = Stack()     # instanting the constructor

stack_obj.push(3)       # calling the method on the object
stack_obj.push(3)       # calling the method on the object
popped_value = stack_obj.__getitem__()

print(popped_value)


class AddingStack(Stack):   # here, Stack is the superclass
    
    def __init__(self):
        Stack.__init__(self)  # explicitly invoke a Superclass constructor  is mandatory
        self.__sum = 0

    def push(self,val):       # overriding the Superclass method
        self.__sum += val
        Stack.push(self,val)

