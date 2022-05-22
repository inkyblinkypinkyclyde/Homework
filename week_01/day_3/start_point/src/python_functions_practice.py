def return_10():
    return 10

def add(a,b):
    c=a+b
    return c

def subtract(a,b):
    c=a-b
    return b

def multiply(a,b):
    c=a*b
    return c

def divide(a,b):
    c=a/b
    return c

def length_of_string(test_string):
    return len(test_string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(a, b):
    c=int(a)+int(b)
    return c

def number_to_full_month_name(m):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    return months[m-1]

def number_to_short_month_name(m):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    return months[m-1][0:3]

def volume_of_cube(a,b,c):
    d=a*b*c
    return d

def reverse_string(string):
    return string[::-1]

def fahrenheit_to_celsius(f):
    c = (f-32)*(5/9)
    return c
