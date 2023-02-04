from prettytable import PrettyTable
import numpy as np
import smtplib
import time
import random
import pandas as pd
def final_restaurant():
    counter = 1
    purchases = []
    favorites = []
    item_price = [["Wheat Bread",2.50],["Multigrain Bread",2.10],["Chocolate Muffin",1.00],["Blueberry Muffin",1.00],["Vanilla Muffin",1.00],["Chocolate Cake",10.50],["Bread Cake",9.10],["Strawberry Cake",10.40],["Black Forest Cake",12.40],["Strawberry Muffin",1.00],["Cinnamon Roll",1.00],["Baguette",1.10],["Birthday Cake (Custom)",11.50],["Chicken Noodles",5.99],["Vegetarian Noodles",5.49],["Manchuria Chicken",7.99],["Chicken Egg Roll",3.99],["Vegetable Spring Roll",3.49],["Parmesan Caesar Salad",5.79],["French Fries",1.10],["Crispy Chicken Nuggets",1.10],["Spicy Chicken Nuggets",1.25],["Crispy Grilled Cheese Sandwich",3.10],["Chicken Caprese Panini",3.75],["Italian Pizza Bites",2.75],["Crispy Cheese Twists",2.99],["Macaroni and Cheese",2.49],["Cheese Sticks",2.99],["Baby Corn",2.30],["Chicken Dumplings",4.60],["Spinach Dumplings",4.60],["Honey Walnut Shrimp",4.50],["Grilled Teriyaki Chicken",4.10],["Chicken Alfredo",7.50],["Shrimp Alfredo",7.50],["Herb-Grilled Salmon",9.50],["Breadsticks",2.50],["Cheese Quesadilla",2.00],["French Toast Sticks",2.99],["Croissant Sandwich",1.99],["Seasoned Potatoes",1.40],["Honey Butter Biscuit",1.25],["Chicken Quesadilla",2.25],["Chow Mein",4.00],["Buffalo Wings",2.99],["Meaty Marinara Pasta",5.50],["Garlic Bread",0.99],["Samosa",1.00],["Crispy Almond Chicken Breast",5.75],["Spicy Chicken Burger",4.49],["Crispy Chicken Sandwich",2.00],["Veggie Burger",1.90],["Cheese Pizza",9.00],["Pepperoni Pizza",10.00],["Supreme Pizza",11.50],["BBQ Chicken Pizza",12.25],["BBQ Pepperoni Pizza",12.25],["Buffalo Chicken Pizza",13.00],["Veggie Pizza",10.00],["Chicken Biryani",8.99],["Shrimp Biryani",9.99],["Vijaywada Biryani",10.00],["Mutton Biryani",9.99],["Original Lemonade",1.19],["Raspberry Lemonade",1.99],["Mango-Strawberry Iced Tea",2.10],["Sweet Iced Tea",2.00],["Cappucino",2.50],["Cold Brew Iced Coffee",2.00],["Chocolate Milk",1.00],["Tropical Berry Lemonade",1.50],["Orange Juice",1.00],["Fruit Punch",1.10],["Iced Expresso",2.25],["Pepsi",0.99],["Fanta",0.99],["Mountain Dew",0.99],["Hot Chocolate",1.05],["Chocolate Chip Cookie",0.50],["Macadamia Nut Cookie",1.20],["Pumpkin Cheesecake",6.99],["Tiramisu",6.79],["Glazed Doughnut",0.95],["Sicilian Cheesecake",5.99],["Chocolate Fudge Sundae",4.99],["Almond Croissant",1.10],["Butter Croissant",1.10],["Triple Chocolate Brownie",3.79],["Cinnamon Sticks",2.99]]
    appetizers = ["Chicken Noodles","Vegetarian Noodles","Manchuria Chicken","Chicken Egg Rolls","Vegetable Spring Rolls","Parmesan Caesar Salad","French Fries","Crispy Chicken Nuggets","Spicy Chicken Nuggets","Crispy Grilled Cheese Sandwich","Chicken Caprese Panini","Italian Pizza Bites","Crispy Cheese Twists","Macaroni and Cheese","Cheese Sticks"]
    entrees = ["Baby Corn","Chicken/Spinach Dumplings","Honey Walnut Shrimp","Grilled Teriyaki Chicken","Chicken/Shrimp Alfredo","Herb-Grilled Salmon","Breadsticks","Cheese Quesadilla","French Toast Sticks","Croissant Sandwich","Seasoned Potatoes","Honey Butter Biscuit","Chicken Quesadilla","Chow Mein","Buffalo Wings","Meaty Marinara Pasta","Garlic Bread","Samosa","Crispy Almond Chicken Breast"]                                                                                                                             
    main_course = ["Spicy Chicken Burger","Crispy Chicken Sandwich","Veggie Burger","Cheese Pizza","Pepperoni Pizza","Supreme Pizza","BBQ Chicken Pizza","BBQ Pepperoni Pizza","Buffalo Chicken Pizza","Veggie Pizza","Chicken Biryani","Shrimp Biryani","Vijaywada Biryani","Mutton Biryani"]
    drinks = ["Original Lemonade","Raspberry Lemonade","Mango-Strawberry Iced Tea","Sweet Iced Tea","Cappuccino","Cold Brew Iced Coffee","Chocolate Milk","Tropical Berry Lemonade","Orange Juice","Fruit Punch","Iced Expresso","Pepsi","Fanta","Mountain Dew","Hot Chocolate"]
    desserts = ["Chocolate Chip Cookie","Macadamia Nut Cookie","Pumpkin Cheesecake","Tiramisu","Glazed Doughnut","Sicilian Cheesecake","Chocolate Fudge Sundae","Almond Croissant","Butter Croissant","Triple Chocolate Brownie","Cinnamon Sticks"]
    bakery_items = ["Wheat Bread","Multigrain Bread","Chocolate Muffin","Blueberry Muffin","Vanilla Muffin","Chocolate Cake","Bread Cake","Strawberry Cake","Black Forest Cake","Strawberry Muffin","Cinnamon Roll","Baguette","Birthday Cake (Custom)"]
    print("Welcome to Macon, a bakery and restaurant! Our hours are from 7:30 A.M. to 10:00 P.M. You may call us at 832-284-3276.")
    people_num = int(input("How many people are we serving today?"))
    print("Okay! Let's move on.")
    name = input("What is your preferred name we shall call you?")

    df1 = pd.read_excel(r"C:\Users\ilsra\Documents\Lakshya - Python\Appetizers-Final2.xlsx")
    df2 = pd.read_excel(r"C:\Users\ilsra\Documents\Lakshya - Python\Entrees-Final2.xlsx")
    df3 = pd.read_excel(r"C:\Users\ilsra\Documents\Lakshya - Python\MainCourse-Final2.xlsx")
    df4 = pd.read_excel(r"C:\Users\ilsra\Documents\Lakshya - Python\Drinks-Final2.xlsx")
    df5 = pd.read_excel(r"C:\Users\ilsra\Documents\Lakshya - Python\Desserts-Final2.xlsx")
    df6 = pd.read_excel(r"C:\Users\ilsra\Documents\Lakshya - Python\BakeryItems-Final2.xlsx")


    menu_now = input("Ok {}. Would you like to view our menu now?".format(name))
    menu_now = menu_now.lower()
    if menu_now == "yes":
        print(df1.to_string(index=False))
        time.sleep(1)
        print(df2.to_string(index=False))
        time.sleep(1)
        print(df3.to_string(index=False))
        time.sleep(1)
        print(df4.to_string(index=False))
        time.sleep(1)
        print(df5.to_string(index=False))
        time.sleep(1)
        print(df6.to_string(index=False))
        time.sleep(4.2)
    cost = 0
    print("For us to make the perfect recomendation for you, we would need to know what type of food you are interested in.")
    choice = input("What type of food are you interested in? We have Appetizers, Entrees, Main Course, Drinks, Desserts, and Bakery Items.") 
    choice = choice.lower()
    if choice == "appetizers":
        print("We would recommend the {} for you.".format(random.choice(appetizers)))
    elif choice == "entrees":
        print("We would recommend the {} for you.".format(random.choice(entrees)))
    elif choice == "main course":
        print("We would recommend the {} for you.".format(random.choice(main_course)))
    elif choice == "drinks":
        print("We would recommend the {} for you.".format(random.choice(drinks)))
    elif choice == "desserts":
        print("We would recommend the {} for you.".format(random.choice(desserts)))
    elif choice == "bakery items":
        print("We would recommend the {} for you.".format(random.choice(bakery_items)))
    purchase_amount = int(input("How many purchases would you like to make?"))
    list5 = []
    for j in range(0,purchase_amount):
        purchase = input("What is your order?")
        purchase = purchase.title()
        purchases.append(purchase)
    for i in range(0,len(item_price),1):
        for k in purchases:
            if k == item_price[i][0]:
                cost += item_price[i][1]
                list5.append(item_price[i][1])
    if len(purchases) >= 4 and len(purchases) < 7:
        print("That sounds like a feast to me!")
    elif len(purchases) >= 7:
        print("Woah! I'm getting jealous of that food!")
    print("The total cost for your purchases was ${}.".format(cost))
    print("Your order is coming with {} tasty treat(s)!".format(people_num))

    print("We are presenting you with three options. You can let us delivery the food to your house, you can take-out, or you can dine in.")
    option = input("Which option would you like to choose?")
    option = option.lower()
    if option == "delivery":
        print("We will be doing that.")
        got_d = True
        delivery = 0.01 * cost
        delivery = round(delivery,2)
        cost = cost + delivery
        cost = round(cost,2)
        print("The total cost for your purchases was ${}.".format(cost))
    elif option == "take-out":
        print("We will be letting you do that.")
        got_d = False
    elif option == "dine in":
        print("We will be ready for you.")
        got_d = False

    parti = input("Would you like to participate in our random number raffle event to get a 20 percent off on your food?")
    parti = parti.lower()
    if parti == "yes":
        rand = random.randint(1,10)
        print("We have picked a number between 1 to 10. You will get three guesses.")
        for i in range(0,3,1):
            guess = int(input("What is your guess?"))
            if guess == rand:
                print("You got it!")
                got = True
                discount = 0.2 * cost
                discount = round(discount,2)
                cost = cost - discount
                cost = round(cost,2)
                print("The updated cost for your purchases was ${}.".format(cost))
                break
            elif guess != rand:
                print("So close!")
                got = False
            elif guess > rand:
                print("Your guess was not between 1 and 10.")
        print("The random number was {}.".format(rand))
    elif parti == "no":
        print("That's okay! We believe everyone has their opinion.")
        
    open_fav = input("Would you like to open a favorites account?")
    open_fav = open_fav.lower()
    if open_fav == "yes":
        print("Ok! Let's get started!")
        fav_amount = int(input("How many favorites would you like to add to your account?"))
        for i in range(0,fav_amount,1):
            favorite_name = input("What is your favorite {}?".format(counter))
            favorites.append(favorite_name)
            counter = counter + 1
        print("Good job opening your favorites account! We just need to make sure if we got the right information.")
        print("Are these your correct favorite(s)?")
        for i in favorites:
            print(i)
        correct = input(" ")
        correct = correct.lower()
        if correct == "yes":
            print("Okay!")
        elif correct == "no":
            change = input("What would you like to change in your favorites?")
            if change in favorites:
                print("Okay!")
                change_to = input("What would you like to change {} to?".format(change))
                favorites.remove(change)
                favorites.append(change_to)
                print("Here are your updated favorites:")
                for i in range(0,len(favorites)):
                    print(favorites[i])
        elif change not in favorites:
            change = change.upper()
            print("{} was not found in your favorites list.".format(change))
    elif open_fav == "no":
        print("That's okay! We will move on then.")

    receipt = input("Would you like a receipt?")
    receipt = receipt.lower()
    counter_receipt =  0
    if receipt == "yes":
        table1 = PrettyTable(["Item Name","Item Price"])
        for i in range(0,len(purchases)):
            table1.add_row([purchases[i],list5[counter_receipt]])
            counter_receipt = counter_receipt + 1
    if got == True:
        table1.add_row(["Discount:",discount])
    elif got_d == True:
        table1.add_row(["Delivery Fee: ", delivery])
    else:
        pass
    table1.add_row(["TOTAL:",cost])
    print(table1)

    review = int(input("How many stars out of 5 would you rate us for our service?"))
    if review == 5:
        print("Our team at Macon is glad we could meet your expectations.")
        print("Thank you for shopping at Macon! We hope to see you again!")
    elif review == 4 or review == 3:
        print("Our team at Macon is sure we can do a little better next time. We're content on how we served you today.")
        print("Thank you for shopping at Macon! We hope to see you again!")
    elif review == 2 or review == 1:
        print("Our team at Macon is deeply disappointed on how we served you today. We will do better next time.")
        print("Thank you for shopping at Macon! We hope to see you again!")
    elif review == 0:
        print("Our team at Macon will take this feedback very seriously. We are very sorry we couldn't meet your expectations.")
        print("Thank you for shopping at Macon! We hope to see you again!")
    else:
        print("We couldn't process that response because it was invalid.")
        print("Thank you for shopping at Macon! We hope to see you again!")
final_restaurant()
