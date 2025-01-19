#Nussipov Danial Lab 1

#Python Syntax
print("Hello, World!")

if 5 > 2:
  print("Five is greater than two!")

#Python comments
#This is a comment
print("Hello, World!")

print("Hello, World!") #This is a comment

#print("Hello, World!")

#This is a comment
#written in
#more than just one line

"""
This is a comment
written in
more than just one line
"""
#Python Variables
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

#Python Data Types
x = 5
print(type(x)) #int

x = "Hello World"
print(type(x)) #str

x = 20.5
print(type(x)) #float

x = 1j
print(type(x)) #complex

x = ["apple", "banana", "cherry"]
print(type(x)) #list

x = ("apple", "banana", "cherry")
print(type(x)) #tuple

x = {"name" : "John", "age" : 36}
print(type(x)) #dict

x = {"apple", "banana", "cherry"}
print(type(x)) #set

x = True
print(type(x)) #bool

#Pythom Numbers
x = 1    #int
y = 2.8  #float
z = 1j   #complex
print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522
print(type(x)) #int
print(type(y)) #int
print(type(z)) #int

x = 1.10
y = 1.0
z = -35.59
print(type(x)) #float
print(type(y)) #float
print(type(z)) #float

x = 35e3
y = 12E4
z = -87.7e100
print(type(x)) #float
print(type(y)) #float
print(type(z)) #float

x = 3+5j
y = 5j
z = -5j
print(type(x)) #complex
print(type(y)) #complex
print(type(z)) #complex

#Convert from one type to another:
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#random number
import random
print(random.randrange(1, 10))

#Python casting
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x, y, z)

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(x, y, z)

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x, y, z)

#Python strings
print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

#Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)


txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#Slicing strings
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

#Modify Strings
a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip()) #The strip() method removes any whitespace from the beginning or the end

#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))
print(a.split(",")) # returns ['Hello', ' World!']

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Format Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

#Escape Character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)