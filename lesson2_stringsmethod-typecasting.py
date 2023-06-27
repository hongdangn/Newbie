name = "dang"

print(len(name)) #length of the name variable
print(name.find("a")) #find the location of character "a" in the name variable
print(name.capitalize()) #capitalize first letter of the name
print(name.upper()) #all letters in the name are uppercase
print(name.lower()) #all letters in the name are lowercase
print(name.isdigit()) #if all the leters are digits, return true, else, return false
print(name.isalpha()) #if all the letters are the alphabetical characters, return true, else return false
print(name.count("a")) #count how many "a" characters in the name
print(name.replace("a", "Q")) #first letter in the parentheness will be replaced by the second one
print(name*4) #print the name 4 times

#type casting = convert the data type of a value to another data type
x = 1
y = 2.1
z = "3"

y = str(y)
z = float(z)
print(z*3)
print("The value of X is truly" + " " + y)

#looping through a string
for i in banana:
    print(i)

#length of string
x = "Hello, world"
print(len(x))

#check if a certain phrase or character is in the string or not
txt = "hong dang dep trai vay sao"
if "vay" in txt:
    print("Yes, 'vay' is present")
if "tre" not in txt:
    print("No, 'tre' is not present")
