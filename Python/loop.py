'''from asyncio.windows_events import NULL
from dataclasses import fields
import string

form = ["First Name","Middle Name","Last Name","age","Area","City","State","phone","salary"]
dict = {}

for i in range(len(form)):
    inp = input()
    #if form[i]=="First Name":
    if inp==NULL:
        print("ENter valid name!")
        pass
    else:
        print("hi")
'''


from asyncio.windows_events import NULL
from contextlib import nullcontext
from inspect import _empty
import numbers
from queue import Empty
from unicodedata import name


while True:
    fname = input("Enter first name:")
    if fname.isnumeric():
        print("Check your input!")
        pass
    else:
        break

while True:
    lname = input("Enter last name:")
    if lname.isnumeric():
        print("Check your input!")
        pass
    else:
        break

while True:
    ph = input("Enter phone number:")
    if ph.isalpha() or len(ph)<10:
        print("Check your input!")
        pass
    else:
        break

while True:
    age = input("Enter age:")
    if (age is nullcontext) or int(age)<20:
        print("Check your input!")
        pass
    else:
        break

while True:
    city = input("Enter age:")
    if city==NULL:
        print("Check your input!")
        pass
    else:
        break

while True:
    salary = float(input("Enter salary:"))
    if salary==NULL or salary<0:
        print("Check your input!")
        pass
    else:
        break

while True:
    dept = input("Enter department:")
    if dept==NULL or dept.isnumeric():
        print("Check your input!")
        pass
    else:
        break


print(f"\nFull Name: {fname} {lname}")
print(f"Age: {age}")
print(f"Phone Number: {ph}")
print(f"City: {city}")
print(f"Salary: {salary}")
print(f"Department: {dept}")