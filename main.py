# username = input("Type in your code: ")

# invalid = "0123"

# for number in username:
#     if number in invalid:
#         print("This character is not allowed:", number)



# vowels = "aeiou"

# const = "bcdfghijklmnpqrstvwxyz"

# word = input("Enter a word: ")

# vowel_num = 0
# for letter in word:
#     if letter in vowels:
#         vowel_num += 1 
#     elif letter in const:
#         vowel_num += 0

# print("There are", vowel_num, "vowels in the word")


# phone_number = input("Type in your phone number: ")

# valid = "0123456789+"

# for number in  phone_number:
#     if number not in valid:
#         print("Not a valid number")


# guest = int(input("Enter number of guest: "))

# for i in range(guest):
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
    
#     if age >= 18:
#         print("Welcome,",name)
#     else:
#         # print("House rules no below 18 drinking, thanks.")



for i in range(5):
    username = input("Enter your username:")
    pass_code = int(input("Enter your passcode: "))
    
    if username == "admin" or "pass_code" == "012345":
        print("Welcome, Admin!")  
        break
        
    if username != "admin" or pass_code != "012345":
        print("You are not the admin")