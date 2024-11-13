destination = input("What is your preferred accommodation choice, Hotel or Resort? ").lower()

if destination == 'resort':
    max_budget = int(input("What is your maximum budget? "))
    if max_budget >= 350:
        print("The Six Senses Resort would be a perfect choice")
    else:
        print("Check out Four Seasons Resort")

else:
    print("Check out the nearest Hilton")




    
