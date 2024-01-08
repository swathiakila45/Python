#Password Generator Project
import random
# anime = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
anime=["luffy","sanji","zoro","robin","nami","brook","franky","usopp","chopper","jimbei"]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print()
print()

print("Welcome to the PyPassword Generator!")
nr_anime= int(input("How many anime would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password=""

# for letter in range(0,nr_anime):
#     password+=random.choice(anime)
# for symbol in range(0,nr_symbols):
#     password+=random.choice(symbols)
# for number in range(0,nr_numbers):
#     password+=random.choice(numbers)
# print(password) 


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password=[]

for letter in range(0,nr_anime):
    #note : instead of append the string concatenation operator also works for lists 
    random_name=random.choice(anime)
    print("Random name chosen "+random_name)
    password+=random_name
    # print(password)
for symbol in range(0,nr_symbols):
    password+=random.choice(symbols)
for number in range(0,nr_numbers):
    password+=random.choice(numbers)

random.shuffle(password)
print("\n")
print("Generated password "+"".join(password))
print()
print("\n\n")
