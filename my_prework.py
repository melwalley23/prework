# Question !:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_" + user_name + "!")

hello_name('USERNAME')

# Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
    for value in range(1, 100, 1):
        return value

first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been define below.

def max_num_in_list(a_list):
    max = a_list[0]
    for list in a_list:
        print("The max number is currently:", max)
        if list > max:
            max = list
    return max
max_num_in_list([888, 7789, 654, 961])

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100,
# unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if (a_year%4) == 0:
        if (a_year%100) == 0:
            if (a_year%400)== 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
year = int(input("Please enter a year (e.g 2020)" ))

if is_leap_year(year):
    print(str(year) + " is a leap year.")
    print("It contains 366 days.")
else:
    print(str(year) + " is not a leap year.")
    print("It contains 365 days.")

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    numbers = []
    for value in range(1,8):
        number = value**1
        numbers.append(number)
    a_list = numbers
    print(a_list)

is_consecutive(a_list=True)