# counter = 0

# while counter < 3:
#     name = input("Enter your name: ")
#     print("Congrats!",name,"You saved 20%")
#     counter += 1
# print("All done")
     

tries = 0 

code = ""

while tries < 5 and code != 'python':
    code = input("Enter a programming language: ")
    tries += 1

if code == 'python':
    print("It took you",tries,"number of tries")


