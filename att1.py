"""
Follow the instructions explained in the problem video and try to implement a solution on your own. Compare it with my solution (video + downloadable files) thereafter.

1) Create two variables – one with your name and one with your age

2) Create a function which prints your data as one string

3) Create a function which prints ANY data (two arguments) as one string

4) Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)
"""

name = input('user name: ')
age = input('User age: ')

def data_as_string():
    return print(name + ' - ' + age)

data_as_string()

def print_two_args(data1, data2):
    return print(data1 + ' - ' + data2)

print_two_args(name, age)

def decades_lived(age):
    decades = age // 10
    print(decades)

decades_lived(int(age))
