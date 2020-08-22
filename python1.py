# --- GeekMustHave Python - Getting Started
  
# --- All this just to clear the screen???
import os
_=os.system("clear")

message = "GeekMustHave, Python Journeys - Getting started "
message += "11/21/2018 Happy Learning Day"
print(message)

# --- Def is the equilivant of function
#     DocString can be first line of Def triple double-quotes """Description"""
#     DocString like a help for the DEF (Function)

def double(num):
  """Function to double the value sent to it"""
  return num*2

print(double(4))  #--- Run the function
print(double.__doc__)  #--- Show documentation about function

# --- Multiple variables, one line
firstName, lastName, age, pi = 'John', 'Schuster', 65, 3.1415

print("First name: " + firstName)
print("Last Name: " + lastName)
print("My age: " + str(age))  #--- standard (str) function
print("Piece of Pi: " + str(pi))
print("Pi Age: " + str(age * pi))

import constant
print(constant.PI)   #--- Not the same as lowercase (pi)

# --- Lists [] [] [] [] [] 
a = [5,10,12,32,118]
print('Forth item in list: ' + str(a[3]))  #--- should be 32 as lists are zero based index
a[3]=988
print('Forth item in list: ' + str(a[3]))  #--- should be 988 as lists are zero based index

# --- Tuples - Can't be changed () () () ()
vowels = ('a', 'e', 'i', 'o', 'u')
print("Second item in set: " + vowels[1])

# --- Sets - Unordered lists, not reordered, dups removed {} {} {} {}
ids = {192, 188, 203, 188, 144, 192, 188}
print("Sets: ")
print(ids)

# --- Dictionary - Unordered key:value  {:} {:} {:}, no indexed 0,1,2 access, key only
morse = {'a': ".-", 'b': "_..", 'c': "_._."}
print("Morse for 'a': " + morse['a'])



       