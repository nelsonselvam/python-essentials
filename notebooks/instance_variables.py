class ExampleClass:
    
    def __init__(self, val=1):
        self.first = val
    
    def set_second(self, val):
        self.second = val
        

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.set_second(5)
example_object_3.third = 5


print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

print(example_object_3.first)


class ExampleClass():
     
    def __init__(self, val=1):
         self.__first = val         # makes the instance variable private
        
    '''
    When Python sees that you want to add an instance variable to an object and you're going to 
    do it inside any of the object's methods, it mangles the operation in the following way:

        it puts a class name before your name;
        it puts an additional underscore at the beginning.
    '''
    
    def set_second(self, val=1):
         self.__second = val
    
        
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.set_second(5)
example_object_3.third = 5


print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

