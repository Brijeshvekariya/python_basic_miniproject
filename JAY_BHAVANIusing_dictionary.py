product = {}
total20 = 0
#for while loop flag
status = True
while status:
    print("\n-----------------------------------------------------------------------------------------------------------------------------------------\n")
    menu = """
                                                                Welcome To Jay Bhavani Snacks
                                                                Please Select your Role :

                                1. Press 1 for Manager           2. Press 2 for Customer          3. Quit the Application                      

                    """
    print(menu)
    # tot variable declared for making total
    tot = 0
    role = int(input("Enter your role : "))
    if role == 1:
        flag = True
        print("\n\n")
        print("\n-----------------------------------------\n")
        print("Welcome Sir")
        while flag:
            specific = {}
            print("\nWhat do you want to Do :\n1. Add Food Items \n2. Display Menu \n3. Change Price \n4. Quit ")
            man_choice = int(input("Enter your choice : "))
            if man_choice == 1:
                product_name = input("Enter product name : ").title()
                if product_name in product:
                    print("\n-----------------------------------------\n")
                    print("This food product is already Existing.")
                    print("\n-----------------------------------------\n")
                else:
                    product_qty = int(input("Enter Quantity of the product : "))
                    product_price = int(input("Enter the price of product : "))
                    total20 += product_price
                    #entering data in to child or inner dictionary
                    specific['qty'] = product_qty
                    specific['price'] = product_price
                    #entering data in main dictionary
                    product[product_name] = specific
                    print("\n-----------------------------------------\n")
                    print("Successfully Product added to MENU")
                    print("\n-----------------------------------------\n")
            elif man_choice == 2:
                print("\n-----------------------------------------\n")
                print(product)
                print(total20)
                print("\n-----------------------------------------\n")
            elif man_choice == 3:
                print("\n-----------------------------------------\n")
                #make changes in which product
                find_product = input("Enter name of Product : ").title()
                if find_product in product:
                    print("\nWhat do you want to Do :\n1. Change in Quantity of Product  \n2. Change in Price")
                    change_choice = int(input("Enter your choice : "))
                    if change_choice == 1:
                        product_new_qty = int(input(f"Enter Updated Quantity of {find_product} : "))
                        # make change in quantity of specific product.
                        product[find_product]['qty'] = product_new_qty
                        print("\n-----------------------------------------\n")
                        print(f"Successfully Quantity Updated in {find_product}",)
                        print("\n-----------------------------------------\n")
                    elif change_choice == 2:
                        product_new_price = int(input(f"Enter Updated Price of {find_product} : "))
                        # make changes in price of specific product.
                        product[find_product]['price'] = product_new_price
                        print("\n-----------------------------------------\n")
                        print(f"Successfully Quantity Updated in {find_product}",)
                        print("\n-----------------------------------------\n")
                    else:
                        print("Enter Valid Input.")
                else:
                    print("Enter Valid Product Name.")
            elif man_choice == 4:
                flag = False
            else:
                print("Enter Valid Option.")     
    elif role == 2:
        print("\n-----------------------------------------\n")
        name = input("Enter Your Name : ").title()
        flag = True
        while flag:
            print("\n-----------------------------------------\n")
            print("                                                MENU\n")
            for food in product.keys():
                # for price in product[food]['price']:
                # for i in range(2,len(product[food])):
                print(f"{food}      -----     Rs. {product[food]['price']}")
            print("\n-----------------------------------------\n")    
            food = input("Enter Product Name you want to Order : ").title()
            if product[food]:
                quantity = int(input("Enter Quantity you want to order : "))
                # checking quantity is available with us or not
                if quantity <= product[food]['qty']:
                    product[food]['qty'] -= quantity
                    # making total
                    total = product[food]['price'] * quantity
                    print("\n-----------------------------------------\n")
                    print("Total Payable Amount : ",total,"/-")
                    print("\n-----------------------------------------\n")
                    cus_choice = input("Do you want to add more (Y or N) : ").upper()
                    tot += total
                    if cus_choice == "Y":
                        pass
                    else:
                        loop = False

                else:
                    print("\n\nSorry Sir/Madam,\n\t\t we could not complete your Order, as We are Out of Stock.")
            else:
                print("Enter Valid Product Name.")
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


            
