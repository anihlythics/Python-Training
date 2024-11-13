print("Could you take out time to rate the product/service out of 1 - 10")

rate = int(input("Rate 1 to 10 according to your satisfaction at the store: "))

if rate >=9:
    print("Thanks for the patronage")
elif rate < 9 and rate >=5:
    suggest = input("Do you mind telling us, how we can make your experience much better? ")
    print(suggest+".")
    print("We will do better")
else:
    print("We are sorry to hear that!")