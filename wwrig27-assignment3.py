# %% [code]
# Note: you must use python 'for loops' for this assignment.
student_name = "William Wright"

# List of vehicle milage
mpg = [18,21,20,21,16,18,18,18,16,20,19,15,17,17,15,15,17,16,14,11,14,13,12,16,15,16,15,15,14,11,11,14,19,22]

# Write your for loop and conditional logic here:

num_items = 0
sum_items = 0 
smallest_num = mpg.sort()
largest_num = mpg.sort()

for num in mpg:
    num_items += 1
    sum_items += num 
    avg_num = sum_items / len(mpg)
    smallest_num = mpg[0]
    largest_num = mpg[-1]

#Output the results
print("The number of items: ", num_items)
print("The sum of the items: ", sum_items)
print("The average of the items: ", avg_num)
print("The smallest number :", smallest_num)
print("The largest number :", largest_num)


# Dictiory of employees
employees = {123: 'Bob', 124: 'Susan', 128: 'Abby', 125: 'Henry', 126: 'Edward', 127: 'James'}


# Write your for loop here and logic here:
emp_numbers = []
emp_names = []

for emp_num, emp_name in employees.items():
    emp_numbers.append(emp_num)
    emp_names.append(emp_name)


# Output the results
print("List of employee numbers: ", emp_numbers)
print("List of employee names: ", emp_names)