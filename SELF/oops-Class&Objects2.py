# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:


# The string representation of an object without the __str__() fucntion:

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("John", 36)

# print(p1)

# THe string representation of an object WITH the __str__() function:

# class Person:
#     def __init__(self, name, age):
#         self.name  = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name}({self.age})"
    
# p1 = Person("John", 36)

# print(p1)

# This type should be used instead of an empty class. use of pass

# class Person:
#     pass









