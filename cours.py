# variabls
"""
print("hello world ! ")
my_name = "aymane"
age = 20
is_student = False
print(f"Hello {my_name} {age} years old")
if is_student is True :
    print("you are student ")
else:
    print("you are not student")
"""
# typecasting = the process to converting a variable from one  data to another to another
#               str() , int() , float() , bool()
"""
name ="aymane"
age = 20
note = 19.5
is_admin = True
print(type(is_admin))
#converting
age = float(age)
print(type(age))
age = str(age)
print(type(age))
"""
# User input
"""
UserName = input("what is your name : ")
UserAge = input("Enter Your Age : ")
UserAge = int(UserAge)
print(type(UserAge))
print(f"Welcome {UserName}")
"""
# Logical operator  = or , and , not
"""
temp = 40
is_raining = False
if temp > 35 or temp < 10 or is_raining:
    print("The outdoor event is cancelled ")
else:
    print("The outdoor event is scheduled")
"""
# While loop = used to repeat a block of code as long a condition remains 'True'
#                   we re-check the condition at the end of the loop
'''
name = input("Enter your name : ")
age = input("Enter your Age : ")
while name == "":
    name = input("Enter your name : ")
    age = input("Enter your Age : ")
print(f"Hello {name}")
'''
# for loop
fruits = ["banana", "appel", "coconut"]
# fruits[0] = "whatermalen"
# fruits.append('whatermalen')
# fruits.remove("banana")
# fruits.pop(0)
# fruits.clear()
for i in fruits:
    print(i, end=' ')
