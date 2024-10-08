# name = input("Enter your name: ")

# result = name.find(" ")
# result = len(name)
# result = name.rfind("q")
# name = name.capitalize() > Bro code
# name = name.title() > Bro Code
# name =name.upper() # convert all words to upper format
# result = name.isdigit() // check num
# result = name.isalpha() // chek alpha //

#phone_number = input("Enter your phone #:")

#result = phone_number.count("-")

#phone_number = phone_number.replace("-", " ")

# you can find more string functions via  print(help(str)) let`s do it
#print(help(str))

#print(result)

#username = input("Enter username:")

#checkSpace = username.find(" ")

#if len(username) > 12:
#    print("Your username is too long")
#elif not username==-1:
#    print("Your username can`t contain spaces")
#else:
#    print(f"Welcome {username}")

# indexing =accessing elements of a  sequence using [] indexing operator
#                       [start : end : step]

card_number ="123456789023"

# print(card_number[0:4])
# print(card_number[:4])
# print(card_number[5:8])
# print(card_number[5:])
# print(card_number[::3]) ## step after 3

last_digit =card_number[-4:]
print(f"XXXX-XXXX-XXXX- {last_digit}")