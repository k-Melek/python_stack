student_1 = ["John", "Mayer", 40, [9.8,10,10], 25] #*List 

#? OOP: Object Oriented Programming
#? CLASS its a blueprint = template = factory to create objects (cars, students , products...)
#* inside class we have (attributes & methods)
#* attributes : what the student can have as Characteristics (nouns)
#* methods : what the student can do. (functions actions inside the class)  (verbs)
#* D.R.Y = Don't Repeat Yourself
#* Model Real Life

student1 = {
    'first_name':"John",
    'last_name': "Mayer",
    'age': 40,
    'marks': [9.8,10,10],
    'fav_number': 25
    } # Dict (in case of student 1,2,3..) Needs CLASS

#! CREATING CLASS (in PascalCase)

class Student:
    #! CONSTRUCTOR
    def __init__(self, first_name, last_name, age, marks, fav_number):
        #attributes ----= Values
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.marks = marks
        self.fav_number = fav_number
    #! METHODS
    def increase_age(self,amount):
        # print("this is self:",self.first_name, self.age, self )
        print("before:",self.age)
        self.age+=amount
        print("after",self.age)
        return None

john = Student("John", "Mayer", 40, [12,35,34], 23)
Alex = Student("Alex", "Max", 35, [12,35,34], 23)
Sarah = Student("Sarah", "Jones", 27, [12,35,34], 23)


# print("********",john,"*******")

# print(f"FN: {john.first_name}\nLN : {john.last_name}\nAGE : {john.age}")
john.increase_age(12)
Sarah.increase_age(8)
Alex.increase_age(20)