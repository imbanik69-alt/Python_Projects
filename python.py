import random
import string


length = int(input("Enter the length of the password : "))
password = " "

digits = string.digits
char = string.ascii_letters
special = string.punctuation
upper = string.ascii_uppercase
lower = string.ascii_lowercase

characters = digits + char + special + upper + lower

for i in range(length):
    password += random.choice(characters)

print(password)

   




    
