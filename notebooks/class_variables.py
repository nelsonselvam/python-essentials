class ExampleClass:
    
    # a property which exists in just one copy and is stored outside any object
    counter = 0
    
    def __init__(self,val=1):
        self.__first = val
        ExampleClass.counter += 1   # this increments the counter whenever the class gets instantiated


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(3)

print(example_object_1.__dict__,example_object_1.counter)
print(example_object_2.__dict__,example_object_2.counter)
print(example_object_3.__dict__,example_object_3.counter)


print()

class ExampleClass1:
    varia = 1
    def __init__(self, val):
        ExampleClass1.varia = val


print(ExampleClass1.__dict__)       # this will have 1 since it is getting printed before instance creation
example_object = ExampleClass1(2)

print(ExampleClass1.__dict__)
print(example_object.__dict__)