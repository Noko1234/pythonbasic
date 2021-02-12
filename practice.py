# a = "beach"
# b = "park"
# amount = 3
# # print("i went to {} and {} {} times this week".format(a, b, amount))
# print("i went to the" + a + "and" + b + str(amount) + "a week" )

# x = {"name" : "ashish","age" : 36}
# print(x['age'])

# a = 20
# b = 10
# print(a % b)

#  # Assignment operator
# a = 5
# a += 2
# print(a)

# # Comparator
#
# print(5 > 5)

#Identity is is not ....membership: in, not in

# data = "Python"
# print("o" in data)

#
# name = "ashis"
# age = 20
# print('name {} age {}'.format(name,age))


# first = 'John'
# last = 'Smith'
# print(first + last + 'is a coder')


# x = 10
# y = 20
# z = x
# print(x is y)
# print(x is z)
# print(x is not y)

# fruits = ['mango','apple','orange']
# for fruit in fruits:
#     print(fruit)

# for a in "kathmandu":
#     print(a)


# colors = ["red","orange","white","black"]
# for x in colors:
#     if x == "white":
#         continue
#         print(x)
#
# for x in range(6):
#     if x==3:
#         break
#     print(x)
# else:
#     print("Finally Finished")

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
# for x in adj:
#   for y in fruits:
#     print(x, y)


# def introduction(name , age=0):
#     print(name,age)
#     if age == 0:
#         print("5 yrs")
#     else:
#         print("0 yrs")
#
# introduction("ram")


# def test(*name,**age):
#     print(name)
#     print(age)
#
# test('ram','sita','gita',b=20, a=50)

# def my_function(**kid):
#     print("his last name is" +kid["last"])
# my_function(fname = "Ashish",last ="Noko")


# def my_function(country ="Nepal"):
#     print("i am from" + country)
# my_function()
# my_function("india")
#

def take_value():
      p = int(input("enter principal"))
      r = int(input("enter rate"))
      t = int(input("enter time"))
      return [p, t, r]


def calculate():
    data = take_value()
    x = data[0]
    y = data[1]
    z = data[2]
    return x * y * z / 100


def display():

    return calculate()

print(display())
