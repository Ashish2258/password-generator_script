import random
import string
#user input
user = int(input("Enter the length of password: "))
#data
small  = string.ascii_lowercase
digit = string.digits
special  = string.punctuation
big = string.ascii_uppercase

#password generator
password = small+digit+special+big

temp = random.sample(password,user)

final = "".join(temp)
print(final)
