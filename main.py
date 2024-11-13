product_1 = int(input("What is the cost of product_A? "))
product_2 = int(input("What is the cost of product_B? "))
product_3 = int(input("What is the cost of product_C? "))

total = product_1 + product_2 + product_3

if product_1 < product_2 and product_2 < product_3:
    total_cost = total * 0.5
    print("Congrats you have a %50 discount on your purchase!", total_cost)

if product_1 > product_2 and product_2 > product_3:
    total_cost = total * 0.66
    print("Congrats you have a 66% discount on your purchase!", total_cost)