
# * 1 

def countdown(number):
    return list(range(number, -1, -1))
print(countdown(5))  

# * 2 

def print_and_return(nums):
    print(nums[0])
    return nums[1]
result = print_and_return([1, 2]) 
print("Returned:", result)  

# * 3 

def first_plus_length(lst):
    return lst[0] + len(lst)
print(first_plus_length([1, 2, 3, 4, 5]))  

# * 4 

def values_greater_than_second(lst):
    if len(lst) < 2:
        return False

    second_value = lst[1]
    new_list = [num for num in lst if num > second_value]
    print(len(new_list))
    return new_list

print(values_greater_than_second([5, 2, 3, 2, 1, 4])) 
print(values_greater_than_second([3]))

# * 5 

def length_and_value(size, value):
    return [value] * size





