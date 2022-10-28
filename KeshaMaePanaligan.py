#Python Syntax
print("Kesha Mae Panaligan-2101")

print("--------------------------------------------------------------------------------")     

#Python Indentation
if 10 > 5:
 print("Ten is greater than two.")

print("--------------------------------------------------------------------------------")     

#Python Variables
#Many Values to Multiple Variables
x, y, z = "Photograph", "Collide", "Unwell"
print(x)
print(y)
print(z)

print("--------------------------------------------------------------------------------")     

#One Value to Multiple Variables
x = y = z = "Photograph"
print(x)
print(y)
print(z)

print("--------------------------------------------------------------------------------")    

#Unpack a Collection
songs = ["Photograph", "Collide", "Unwell"]
x, y, z = songs
print(x)
print(y)
print(z)

print("--------------------------------------------------------------------------------")     

#Output Variables
x = "Music "
y = "heals "
z = "depression"
print(x + y + z)

print("--------------------------------------------------------------------------------") 

#Output Variables in Mathematical Operator
x = 14
y = 12
print(x + y)

print("--------------------------------------------------------------------------------") 

#Global Variables
x = "NFT game"

def myfunc():
  x = "non-fungible token-based"
  print("Axie infinity is " + x)

myfunc()

print("Axie infinity is " + x)

print("--------------------------------------------------------------------------------") 

#Python Numbers 
#int

x = 1
y = 2856
z = -457
print(type(x))
print(type(y))
print(type(z))

print("--------------------------------------------------------------------------------") 

#Float
x = 1.12
y = 3.56
z = -3.45
print(type(x))
print(type(y))
print(type(z))

print("--------------------------------------------------------------------------------") 

#Conversion
x = 5    # int
y = 1.0  # float
z = 8j   # complex

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

print("--------------------------------------------------------------------------------") 

#Python Strings
r = "Kesha"
print(r)

print("--------------------------------------------------------------------------------") 

#Multiline Strings Three Quotes
r = """ I've found that,
  no matter what life throws at me
  music softens the blow. """
print(r)

print("--------------------------------------------------------------------------------") 

#Multiline Strings Three Single Quotes
r = ''' I've found that,
  no matter what life throws at me
  music softens the blow. '''
print(r)

print("--------------------------------------------------------------------------------") 

#String Arrays
e = "Kesha, Mae"
print(e[1])

print("--------------------------------------------------------------------------------") 

#Looping Through a Strings
for e in "CHOSEN":
  print(e)

print("--------------------------------------------------------------------------------") 

#String Length
e = "Kesha, Mae"
print(len(e))

print("--------------------------------------------------------------------------------") 

#Check String
txt = "God is always with us!"
print("always" in txt)

print("--------------------------------------------------------------------------------") 

#used if statement
txt = "God is always with us!"
if "always" in txt:
    print("Yes, the word 'always' is present.")

print("--------------------------------------------------------------------------------") 

#Check if NOT
txt = "God is always with us!"
if "leave" not in txt:
    print("No, the word 'leave' is NOT present.")

print("--------------------------------------------------------------------------------") 

#Slicing Strings
i = "Kesha, Mae!"
print(i[3:4])

print("--------------------------------------------------------------------------------") 

#Slicing From The Start
i = "Kesha, Mae!"
print(i[:4])

print("--------------------------------------------------------------------------------") 

#Slicing To The End
i = "Kesha, Mae!"
print(i[3:])

print("--------------------------------------------------------------------------------") 

#Negative Indexing
i = "Kesha, Mae!"
print(i[-4:-3])

print("--------------------------------------------------------------------------------") 

#Modify Strings
#Upper Case
b = "Kesha, Mae!"
print(b.upper())

print("--------------------------------------------------------------------------------") 
b = "Kesha, Mae!"
print(b.lower())

print("--------------------------------------------------------------------------------") 

#Remove Whitespace
e = "Kesha, Mae! "
print(e.strip()) # returns "Kesha, Mae!"

print("--------------------------------------------------------------------------------") 

#Replace String
e = "Kesha, Mae! "
print(e.replace("R", "K"))

print("--------------------------------------------------------------------------------") 

#Split String
e = "Kesha, Mae! "
print(e.split(",")) # returns ['Kesha', ' Mae!']

print("--------------------------------------------------------------------------------") 

#String Concatenation
a = "Kesha"
b = "Mae"
c = a + b
print(c)

print("--------------------------------------------------------------------------------") 

#String Format
age = 19
txt = "My name is Ron, I am " + age
print(txt)

print("--------------------------------------------------------------------------------") 

#Escape Characters
txt = "We are living in called \"Saint Joseph\" from Lumil."

print("--------------------------------------------------------------------------------") 

#Python Booleans
a = 55
b = 20

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print("--------------------------------------------------------------------------------") 

#Evaluate Values and Variables
#String and Number
print(bool("Kesha"))
print(bool(19))

print("--------------------------------------------------------------------------------") 

#Evaluate 2 Variables
a = "Kesha"
b = 19

print(bool(x))
print(bool(y))

print("--------------------------------------------------------------------------------") 

#Some Values are False
class my_class():
    def _len_(self):
      return 0

myobject = my_class()
print(bool(myobject))

print("--------------------------------------------------------------------------------") 

#Functions can Return a Boolean
def my_function():
    return True

if my_function():
    print("YES!")
else:
    print("NO!")

print("--------------------------------------------------------------------------------") 

#Python Lists
thislist = ["Photograph", "Unwell" , "Collide"]
print(thislist)

print("--------------------------------------------------------------------------------") 

#List Length
thislist = ["Photograph", "Unwell" , "Collide"]
print(thislist)

print("--------------------------------------------------------------------------------") 

#List Items- Data Types
Song = ["Photograph", "Unwell" , "Collide"]
Section = [2101, 2102, 2103, 2104, 2105]
Ident = [True, False, False]

print(type(Song))
print(type(Section))
print(type(Ident))