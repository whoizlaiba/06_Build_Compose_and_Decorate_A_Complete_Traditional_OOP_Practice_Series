# 8. The super() Function
# Assignment:
# # Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person constructor called. Name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  
        self.subject = subject
        print(f"Teacher constructor called. Subject: {self.subject}")


t1 = Teacher("Miss Noor Un Nisa", "Mathematics")


print("Name:", t1.name)
print("Subject:", t1.subject)
