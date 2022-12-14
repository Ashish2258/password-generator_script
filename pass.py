import random
import array

MAX_LEN = 16

l1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
l2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

l3 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
                                        
l4 = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
          
combine = l1+l2+l3+l4

digit = random.choice(l1)
alpha = random.choice(l2)
Alpha = random.choice(l3)
symbol = random.choice(l4)

pas = digit+alpha+Alpha+symbol

for x in range(MAX_LEN - 4):
    pas = pas  + random.choice(combine)

temp = array.array('u',pas)
random.shuffle(temp)

password = ""
for x in temp:
    password = password + x
print(password)
