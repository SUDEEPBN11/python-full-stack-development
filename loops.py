'''

for i in range(0,10):
    print("Day 2nd Started to learn Loops in python")

def add(a,b):
    result = a + b
    print(result)
add(5,5)  

def sub(a,b):
    result = a - b
    print(result)
sub(5,5)

def mul(a,b):
    result = a * b
    print(result)
mul(5,5)   


list = ["CSE","ISE","EC","EEE"]
print(list)
print(list[0])

tuple = {"Software Engineer","Software Developer","AI Engineer"}
print(tuple)
print(tuple)


student = {
    "name": "Sudeep",
    "age": 20,
    "branch": "CSE",
    "college": "GCEM"
}

print(student)

'''
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Sudeep", 20)
s2 = Student("Rahul", 21)

print(s1.name)
print(s2.name)

print(s1.age)
print(s2.age)


