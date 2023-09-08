#creating list one for food name and second for food price
food_name = ["Dabeli","Vadapav"]
food_price = [20,25]

main = True
while main:
    print("\n-----------------------------------------------------------------------------------------------------------------------------------------\n")
    user_selection = """
                                                                Welcome To Jay Bhavani Snacks
                                                                Please Select your Role :

                                1. Press 1 for Manager           2. Press 2 for Customer          3. Quit the Application                      

                    """
    print(user_selection)
    user_choice = int(input("Enter your Choice : "))
    if user_choice==1:
        #password verification
        user_password = input("Enter Password for Manager Login : ")
        if user_password == "1234":
            loop = True
            print("\n\n")
            print("\n-----------------------------------------\n")
            print("Welcome Sir")
            while loop:
                print("\nWhat do you want to Do :\n1. Add Food Items \n2. Display Menu \n3. Change Price \n4. Quit ")
                man_choice = int(input("Enter your choice : "))
                if man_choice == 1:
                    add_food = input("Enter Food Name : ").title()
                    #checking food name is alredy exist in list
                    if add_food in food_name:
                        print("This food product is already Existing.")
                    else:
                        add_price = int(input("Enter price of food : "))
                        # adding elements in foodname list
                        food_name.append(add_food)
                        print(food_name)
                        items = len(food_name)
                        # print(items)
                        # adding price in foodprice list
                        food_price.append(add_price)
                        print("\n-----------------------------------------\n")
                elif man_choice == 2:
                    items = len(food_name)
                    # displaying both list for menu 
                    print("\n                       MENU \n")
                    for i in range(0,items):
                        print(food_name[i], " = ", food_price[i])
                    print("\n\nSuccess")
                    print("\n-----------------------------------------\n")
                elif man_choice == 3:
                    find_food = input("Enter Food name you want to change price = ").title()
                    if find_food in food_name:
                        #finding food_name in list
                        count = 0
                        for i in food_name:
                            if i == find_food:
                                #if finds name then count is store in 'a'
                                a = count
                            else:
                                count+=1
                        food_newprice = int(input("Enter New Price of %s : "%find_food))
                        #'a' is for index of entered food name for changing price
                        food_price.insert(a,food_newprice)
                        print("\n-----------------------------------------\n")
                    else:
                        print("Not Available") 
                else:
                    loop = False
        else:
            print("Enter Valid Password.")
    elif user_choice == 2:
        print("\n-----------------------------------------\n")
        name = input("Enter your Name : ")
        print("\n-----------------------------------------\n")
        total = 0
        tot = 0
        loop = True
        while loop:
            items = len(food_price)
            print("\n-----------------------------------------\n")
            # displaying both list for menu 
            print("\n                       MENU \n")
            for i in range(0,items):
                print(i+1,".",food_name[i], " = ", food_price[i])
            choice = int(input("Enter your choice : "))
            if choice <= len(food_name):
                quantity = int(input("Enter Quantity : "))
                print("\n-----------------------------------------\n")
                total = food_price[choice-1] * quantity
                print("Total Payable Amount : ",total,"/-")
                print("\n-----------------------------------------\n")
                cus_choice = input("Do you want to add more (Y or N) : ").upper()
                tot += total
                if cus_choice == "Y":
                    pass
                else:
                    loop = False
            else:
                print("Enter valid product")
        
        print("\n-----------------------------------------\n")
        
        print("Total Amount to be Paid : Rs.",tot)
        print("\n-----------------------------------------\n")
        print("Dear ",(name.title()))
        print("\t\tYou Have to pay Rs. %d /- "%(tot))
        print("\t\t\t\t\t Thank You For Visitng JAY BHAVANI SNACKS ")
        input()
    else:
        quit = input("Enter password to Quit the Application : ")
        if quit == "bhavani":
            main = False
        else:
            main = True
            print("Wrong Password")

            
