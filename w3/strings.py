#PYTHON STRINGS
print("Hello")
print('Hello') #'hello' is the same as "hello"

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a) #Assign String to a Variable

a = "Hello, World!"
print(a[1]) #Strings are Arrays

for x in "banana":
  print(x) #Looping Through a String

a = "Hello, World!"
print(len(a)) #String Length

#Check string
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



#SLICING STRINGS
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5]) #Slice From the Start

b = "Hello, World!"
print(b[2:]) #Slice To the End

b = "Hello, World!"
print(b[-5:-2]) #Negative Indexing



#MODIFY STRINGS
a = "Hello, World!"
print(a.upper()) #Upper Case

a = "Hello, World!"
print(a.lower()) #Lower Case

a = " Hello, World! "
print(a.strip()) # Removes Whitespace

a = "Hello, World!"
print(a.replace("H", "J")) #Replace String

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 



#CONCATENATE STRINGS
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c) #To add a space between them



#FORMAT STRINGS
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)



#ESCAPE CHARACTERS
txt = "We are the so-called \"Vikings\" from the north."

#\'      Single Quote
#\\      Backslash
#\n    	 New Line
#\r      Carriage Return
#\t      Tab
#\b      Backspace
#\f      Form Feed
#\ooo    Octal value
#\xhh    Hex value


