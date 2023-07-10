# This is a comment this line will not be interpeted

"""
This is 
a multi-line Comment
wil not be interpreted
"""
#  How to declare Variables
#  in JavaScript: var variableName = value

#  python is snake we are going to use snake_case_naming_convention

variable_name = "value"

GLOBAL_VARIABLE = "python"

PORT = 5000
APP_NAME = "WEB_APP"

# DATA TYPES

#* Primetives
    #* String
first_str ="hello world"
name="John"
    #* Numbers
        #*integers
age = 41
        #*Floats
bmi = 2.75
        #*Boolean
voted = True
is_admin= False
    #* NoneType
permit = None

# print(name, age, bmi, is_admin)

# print(f"User name: {name} his {age} years and his BMI equal to {bmi}")

# print(f"USER : {name} \nBMI : {bmi}")

# print("FORMAT ** User name: {} his {} years and his BMI equal to {}" .format(name, age, bmi))

# print(f"None :{type(permit)}\nName : {type(name)} \nAge :{type(age)} \nBMI : {type(bmi)} \nADMIN : {type(is_admin)}")

str_age = str(age)
float_age = float(age)
# print(f"AGE : {type(age)} \nSTR_AGE {type(str_age)} \nFLOAT_AGE{type(float_age)} {float_age}")

# print(len(name), name.upper(), first_str.split(' '))


# * COMPLEX LISTS

# Array in JavaScript == List in Python
# INDEX 0------->len(list)-1

my_list = [1,2,3,"45",4,5, name, age, is_admin, bmi, ["yes", "no", None]]

# print(my_list[0])

# print(my_list[0:5])

# print(my_list)
# my_list.append(first_str)
# print(my_list)
# my_list.pop()
# print(my_list)
# my_list.pop(-2)

# numbers = [2,0,22,5,-11,100]
# numbers.sort(reverse=True)
# print(numbers)

# * COMPLEX JavaScript OBJECTS = (PYTHON Dictionaries)
# * Key-Value PAIRS
user = {
    'first_name' : name,
    'last-name' : "smith",
    'age' : age,
    'is_admin' : False,
    'marks' : [10,9,8,10],
    'friends' : {'one' : "Alex" , 'two' : "Max"}
}

# bracker notation
print(user["first_name"])
# .get Notation
print(user.get("is_admin"))

user["is_admin"] = True
print(user)

# * Tuples ( Similar to lists BUT immutable : Can NOT be changed)

my_tuple =(1,2,3)
my_tuple.append(4)

# * SR
my_set = {1,2,2,3,4,5,5,6,"john","john"}
print(my_set)