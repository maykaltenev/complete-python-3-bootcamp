# Variables
# a = 5.1

# print(a)
# a = a + a
# print(a)
# print(type(a))
# my_income = 100
# tax_rate = 0.1
# my_taxes = my_income * tax_rate
# print(my_taxes)

# Strings
name = "hello"
lastName = "world"
doubleName = " I'm going on a run "
print(doubleName)
print('Hello \n world')
print(len("hello"))
print(len("I am"))
# Indexing And Slicing With Strings

mystring = "Hello World"
print(mystring[-2])
print(mystring[:1])
print(mystring[3:6])
print(mystring[::])
# Write your string index below
# Start with 'Hello World'
# and make sure to match spaces and capitalization exactly
print("Hello World"[-3])
print('tinker'[1:4])
name = "Sam"
last_letters = name[1:]
new_name = "P" + last_letters
print(new_name)
x = "hello world"
print(x.upper())
print(x.split())

print("This is string {}".format("INSERTED"))
result = 100 / 777

print("The result {r:1.2f}".format(r=result))
name = "Jose"
print(f"Hello, his name is {name}")
print('Python %s!' % 'rules')
print([2, 'three', 42.17, 'first'])
prices_lookup = {'apples': 2.00, 'oranges': 1.99, 'lemons': 2.5}
print(prices_lookup['apples'])
d = {'k1': 123, 'k2': 131, 'k3': [1, 3, 4], 'k4': {'insideKey': 100}}
print(d['k4']['insideKey'])

with open('myfile.xlsm', 'w') as file:
    file.write("This is the first line.\nThis is the second line.")
