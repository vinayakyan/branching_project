'''
    main.py contains the logic for calculating addition of odd numbers as well as addition of even numbers.
    This is a docstring of main.py
'''

print("Program Starts")

add = 0
for i in range(0,50,2):
    add += i

print("Addition of Even numbers is :", add)

odd_add = 0

for i in range(1,50,2):
    odd_add += i

print("Additon of odd numbers is :", odd_add)

print("Program Ends")