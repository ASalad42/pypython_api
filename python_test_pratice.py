
# def user_name():


arr = [1,2,3,4,5]

for e in arr:
    print (e)


# AND

# list is mutable and tupple is immutable

# yes can add element in tuple

# yes multiple data types

# dictionary

# object_dev = DevOps()

# arr.append(5)

def func(course):
    if course == "devops":
        return True
    else:
        return False

# from file import class Y
# class Z(Y):
#     def __init__(self):
#         super().__init__()


def odd_even(lst,value):

    for e in lst:
        if e == value and [] % 2 ==0:
            return True
        else:
            return False
print(odd_even([1,2,3],3))

def mul(value1, value2):
    if value1 !=0 and value2 !=0:
        return value1 * value2

def div(value1, value2):
    if value1 !=0 and value2 !=0:
        return value1 / value2

def per(value1, value2):
    if value1 !=0 and value2 !=0:
        return (value1 / value2) * 100
# print(per(5,10) > 50%

def dob(value1, value2):
    if value1 !=0 and value2 !=0:
        return (f"your b day is in month {value1} year {value2}")

print(dob(6,98))


def oddeven(num):
    l = list(range(num+1))
    lst = []
    for e in l:
        if e % 2 == 0:
            lst.append("even")
        else:
            lst.append("odd")
    return lst
print(oddeven(10))




def shopp(lst):
    for values in lst.values():
        return sum(lst.values())

shopp_list = {
        "milk": 3.4,
        "bread": 5.5,
        "eggs":6,
        "apples":7,
        "butter": 2
    }
print(shopp(shopp_list))