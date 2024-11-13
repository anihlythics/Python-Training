user_decide = input("Hello, would you like some movie recommendation tonight? ").lower()

if user_decide == "yes":
    print("Lovely, make a choice from the next prompt.")

    movie_choice = input("Which movie genre would you prefer to watch from comedy, action or thriller? ").lower()
    
    if movie_choice == "comedy":
        print("For tonight we would recommend the movie, Hangover Trilogy!, enjoy")
    elif movie_choice == "action":
        print("You might enjoy some packed action like Top Gun!, enjoy")
    elif movie_choice == "thriller":
        print("A great thriller choice would be Inception!, enjoy")
    else:
        print("Sorry, only pick from the available genre.")
else:
    print("Looks like you are tired tonight, good night")