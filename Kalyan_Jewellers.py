makingring = 800
makingneck = 900
makingchain = 850
gold = 5604
name=(input("Enter your Name : "))
gender = (input("Enter your Gender(M or F) : "))
age=int(input("Enter your Age : "))
print("\n")
print("Our Product List : \n")
print("1. Rings ")
print("2. Necklace ")
print("3. Chains \n")
choice=(input("Enter your choice: "))
gram=int(input("Enter product grams : "))
print("Current Gold price is : %d"%gold)
# print(gold)
print("\n-----------------------------------------\n")
print("total price of Gold is : %d"%(gold*gram))
print("\n-----------------------------------------\n")
if choice == "rings" or choice == "Rings" or choice == '1':
    making = makingring
    print("Making Charges of 1 Gram Gold is : 800/-")
    print("Total Making Charges of Ring is : %d"%(making*gram))
    print("\n-----------------------------------------\n")
    total = (gold*gram)+(gram*making)
    print("Total Amount of Ring is : %d"%(total))
    print("\n-----------------------------------------\n")
    if gender == 'M' or gender == 'm' :
        if age >=65 : 
            if total >=100000 and total<300000 :
                print("Discount Available for you is : 20% ")
                dis = (total*20)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
            elif total >= 300000:
                print("Discount Available for you is : 25% ")
                dis = (total*25)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
            else:
                print("Discount Available for you is : 15% ")
                dis = (total*15)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))

        else:
            if total >=100000 and total<300000 :
                print("Discount Available for you is : 15% ")
                dis = (total*15)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
            elif total >= 300000:
                print("Discount Available for you is : 20% ")
                dis = (total*20)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
            else:
                print("Discount Available for you is : 10% ")
                dis = (total*10)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
    else : 
        if age >=65 :  
            if total >=100000 and total<300000 :
                print("Discount Available for you is : 25% ")
                dis = (total*20)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
            elif total >= 300000:
                print("Discount Available for you is : 30% ")
                dis = (total*25)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
            else:
                print("Discount Available for you is : 20% ")
                dis = (total*15)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
        else:
            if total >=100000 and total<300000 :
                    print("Discount Available for you is : 20% ")
                    dis = (total*15)/100 
                    print("After Discount Total Amount of Ring is : %d"%(dis))
                    print("\n-----------------------------------------\n")
                    tot = total+dis
                    print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                    print("\n-----------------------------------------\n")
                    print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                    tax = (tot * 3)/100
                    print("Total Tax to be paid : %d"%tax)
                    print("\n-----------------------------------------\n")
                    final=tot+tax
                    print("Total Payable Amount : %d"%(final))
            elif total >= 300000:
                    print("Discount Available for you is : 25% ")
                    dis = (total*20)/100 
                    print("After Discount Total Amount of Ring is : %d"%(dis))
                    print("\n-----------------------------------------\n")
                    tot = total+dis
                    print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                    print("\n-----------------------------------------\n")
                    print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                    tax = (tot * 3)/100
                    print("Total Tax to be paid : %d"%tax)
                    print("\n-----------------------------------------\n")
                    final=tot+tax
                    print("Total Payable Amount : %d"%(final))
            else:
                print("Discount Available for you is : 15% ")
                dis = (total*10)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
    # for necklace
elif choice == "Necklace" or choice == "necklace" or choice == '2':
    making = makingneck
    print("Making Charges of 1 Gram Gold is : 900/-")
    print("Total Making Charges of Ring is : %d"%(making*gram))
    print("\n-----------------------------------------\n")
    total = (gold*gram)+(gram*making)
    print("Total Amount of Ring is : %d"%(total))
    print("\n-----------------------------------------\n")
    if gender == 'M' or gender == 'm' :
        if age >=65 : 
            if total >=100000 and total<300000 :
                print("Discount Available for you is : 20% ")
                dis = (total*20)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
            elif total >= 300000:
                print("Discount Available for you is : 25% ")
                dis = (total*25)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
            else:
                print("Discount Available for you is : 15% ")
                dis = (total*15)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
        else:
            if total >=100000 and total<300000 :
                print("Discount Available for you is : 15% ")
                dis = (total*15)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
            elif total >= 300000:
                print("Discount Available for you is : 20% ")
                dis = (total*20)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
            else:
                print("Discount Available for you is : 10% ")
                dis = (total*10)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
    else : 
        if age >=65 :  
            if total >=100000 and total<300000 :
                print("Discount Available for you is : 25% ")
                dis = (total*20)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
            elif total >= 300000:
                print("Discount Available for you is : 30% ")
                dis = (total*25)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
            else:
                print("Discount Available for you is : 20% ")
                dis = (total*15)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
        else:
            if total >=100000 and total<300000 :
                    print("Discount Available for you is : 20% ")
                    dis = (total*15)/100 
                    print("After Discount Total Amount of Ring is : %d"%(dis))
                    print("\n-----------------------------------------\n")
                    tot = total+dis
                    print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                    print("\n-----------------------------------------\n")
                    print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                    tax = (tot * 3)/100
                    print("Total Tax to be paid : %d"%tax)
                    print("\n-----------------------------------------\n")
                    final=tot+tax
                    print("Total Payable Amount : %d"%(final))
            elif total >= 300000:
                    print("Discount Available for you is : 25% ")
                    dis = (total*20)/100 
                    print("After Discount Total Amount of Ring is : %d"%(dis))
                    print("\n-----------------------------------------\n")
                    tot = total+dis
                    print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                    print("\n-----------------------------------------\n")
                    print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                    tax = (tot * 3)/100
                    print("Total Tax to be paid : %d"%tax)
                    print("\n-----------------------------------------\n")
                    final=tot+tax
                    print("Total Payable Amount : %d"%(final))
            else:
                print("Discount Available for you is : 15% ")
                dis = (total*10)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
#    for chain
elif choice == "Chains" or choice or choice == '3' :
    making = makingchain
    print("Making Charges of 1 Gram Gold is : 900/-")
    print("Total Making Charges of Ring is : %d"%(making*gram))
    print("\n-----------------------------------------\n")
    total = (gold*gram)+(gram*making)
    print("Total Amount of Ring is : %d"%(total))
    print("\n-----------------------------------------\n")
    if gender == 'M' or gender == 'm' :
        if age >=65 : 
            if total >=100000 and total<300000 :
                print("Discount Available for you is : 20% ")
                dis = (total*20)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
            elif total >= 300000:
                print("Discount Available for you is : 25% ")
                dis = (total*25)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
            else:
                print("Discount Available for you is : 15% ")
                dis = (total*15)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
        else:
            if total >=100000 and total<300000 :
                print("Discount Available for you is : 15% ")
                dis = (total*15)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
            elif total >= 300000:
                print("Discount Available for you is : 20% ")
                dis = (total*20)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
            else:
                print("Discount Available for you is : 10% ")
                dis = (total*10)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
    else : 
        if age >=65 :  
            if total >=100000 and total<300000 :
                print("Discount Available for you is : 25% ")
                dis = (total*20)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
            elif total >= 300000:
                print("Discount Available for you is : 30% ")
                dis = (total*25)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
            else:
                print("Discount Available for you is : 20% ")
                dis = (total*15)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%tax)
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))
        else:
            if total >=100000 and total<300000 :
                    print("Discount Available for you is : 20% ")
                    dis = (total*15)/100 
                    print("After Discount Total Amount of Ring is : %d"%(dis))
                    print("\n-----------------------------------------\n")
                    tot = total+dis
                    print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                    print("\n-----------------------------------------\n")
                    print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                    tax = (tot * 3)/100
                    print("Total Tax to be paid : %d"%tax)
                    print("\n-----------------------------------------\n")
                    final=tot+tax
                    print("Total Payable Amount : %d"%(final))
            elif total >= 300000:
                    print("Discount Available for you is : 25% ")
                    dis = (total*20)/100 
                    print("After Discount Total Amount of Ring is : %d"%(dis))
                    print("\n-----------------------------------------\n")
                    tot = total+dis
                    print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                    print("\n-----------------------------------------\n")
                    print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                    tax = (tot * 3)/100
                    print("Total Tax to be paid : %d"%(tax+1))
                    print("\n-----------------------------------------\n")
                    final=tot+tax
                    print("Total Payable Amount : %d"%(final))
            else:
                print("Discount Available for you is : 15% ")
                dis = (total*10)/100 
                print("After Discount Total Amount of Ring is : %d"%(dis))
                print("\n-----------------------------------------\n")
                tot = total+dis
                print("Total Payable Amount (excluding Taxes) : %d"%(tot+1))
                print("\n-----------------------------------------\n")
                print("I.G.S.T : 1.5% \n C.G.S.T : 1.5%")
                tax = (tot * 3)/100
                print("Total Tax to be paid : %d"%(tax+1))
                print("\n-----------------------------------------\n")
                final=tot+tax
                print("Total Payable Amount : %d"%(final))

print("\n-----------------------------------------\n")
print("Dear ",(name))
print("\t\tYou Have to pay Rs. %d /- "%(final))
print("\t\t\t\t\t Thank You For Visitng KALYAN JEWELLERS ")