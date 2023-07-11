
#! METHODS
# Instance methods parameter SELF
# Have access to instance attributs can change them
# NOTE :have no decorator




class Student:
    #! CLASS Attributes
    school = "MIT"
    #! List to Store all the students that belong to student Class
    all_students = []
    #! CONSTRUCTOR
    def __init__(self, first_name, last_name, age, marks, fav_number):
        #*instance attributes  ----= Values
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.marks = marks
        self.fav_number = fav_number
        Student.all_students.append(self)
        self.car = None
    #! METHODS
    def increase_age(self,amount):
        # print("this is self:",self.first_name, self.age, self )
        print("before:",self.age)
        self.age+=amount
        print("after",self.age)
        return None
    
    def __repr__(self) :
        return f"STUDENT FIRST NAME: {self.first_name}"
    
    def change_name(self, new_name):
        self.first_name = new_name
        return None

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
        return None

    @staticmethod
    def  validate(dict_data):
        is_valid = True
        if len(dict_data['first_name']) < 2 :
            is_valid = False
        if len(dict_data['last_name']) < 2 :
            is_valid = False
        if dict_data['age']  < 17 :
            is_valid = False
        return

class Car:
    #CONSTRUCTOR
    def __init__(self, data_dict):
        self.make = data_dict['make']
        self.model = data_dict['model']
        self.year = data_dict['year']
        self.color = data_dict['color']
        self.miles = data_dict['miles']
    def drive(self):
        self.miles+=10
        print(f"Your car new millage :{self.miles}")
    def beep(self):
        print("BEEP !!!")

honda_data = {
    'make':"Honda",
    'model':"M1"
    
}

honda = Car('Honda', 'M1', 2020, 'Red')
golf = Car('WV', 'Golf 7', 2020, 'Black', 100)
# print(honda.miles)
# print(golf.miles)

honda.drive()

john = Student("John", "Mayer", 40, [12,35,34], 23)
alex = Student("Alex", "Max", 35, [12,35,34], 23)
sarah = Student("Sarah", "Smith", 27, [12,35,34], 23)


# print(john.school)
# print(alex.school)
# print(sarah.school)
# print(Student.all_students)

# for student in Student.all_students:
#     print(student.car)
#     print(student.first_name)
#     print(student.increase_age(2))
#     print("-----------")

# john.change_name("jane")
# Student.change_school("CAMBRIDGE")