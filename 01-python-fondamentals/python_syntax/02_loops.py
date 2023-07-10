"""
In JavaScript
for(var i=0;i<10;i++){
    console.log(i)
}
"""

# IN PYTHON
"""
range = function that return sequence of numbers
start = inclusive has as default value of 0
stop = exclusive and required
step = not required and default value of 1 can be + or -
""" 

# for i in range(0,10):
#     print(i)

# for i in range(0,10,2):
#     print(i)
#     for j in range(0,i):
#         print(j)

super_heroes = ["superman", "batman", "spiderman", "antman", "jedi"]
# for i in range(0,len(super_heroes)):
#     print(super_heroes[i])

# for hero in super_heroes:
#     print(hero)

# my_list = [1,2,3,"45",4,5, ["yes", "no", None]]
# for element in my_list:
#     print(element)

user = {
    'first_name' : "John",
    'last-name' : "smith",
    'age' : "41",
    'is_admin' : False,
    'marks' : [10,9,8,10],
    'friends' : {'one' : "Alex" , 'two' : "Max"}
}
for key,value in user.items():
    print(f"KEY : {key} --- Value : {value}")