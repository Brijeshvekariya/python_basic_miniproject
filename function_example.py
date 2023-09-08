def printline():
    print("*"*40)
    print()
def factorial():
    fact = 1
    num = int(input("Enter Any Number : "))
    for i in range(1,num+1,):
        fact *=i
    return fact
def max3():
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))
    num3 = int(input("Enter Third Number : "))
    if num1>num2 and num1>num3:
        print(f"{num1} is Maximum from three Numbers")
    elif num1>num2 and num1<num3:
        print(f"{num3} is Maximum from three Numbers")
    else :
        if num2>num3:
            print(f"{num2} is Maximum from three Numbers")
        else:
            print(f"{num3} is Maximum from three Numbers")
def max2():
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))
    if num1>num2:
        print(f"{num1} is Greater than {num2}")
    else:
        print(f"{num2} is Greater than {num1}")
def fibonacci():
    n = int(input("Enter number of digit : "))
    n0 = 0
    n1 = 1
    print("The Fibanocci Series is ",n0,end=", ")
    for i in range(0,n):
        print(n1,end=", ")
        next = n0+n1
        n0 = n1
        n1 = next

def evenodd(num):
    if num%2==0:
        return f'{num} is Even Number'
    else:
        return f"{num} is Odd Number"

def natural(n):
    sum = 0
    for i in range(0,n+1):
        sum+=i
    return sum
    


status = True
while status:
    menu = '''
                                        MENU

        1. Factorial of any Number
        2. Find Maximum from three Number
        3. Find Maximum of Two Number 
        4. Fibonacci series 
        5. Even or Odd
        6. Sum of Natural Numbers
        7. Exit
    
    
    '''
    print()
    print(menu)
    choice = int(input("Enter your Choice : "))
    if choice == 1 : 
        printline()
        print("The Factorial is ",factorial())
    elif choice == 2:
        printline()
        max3()
    elif choice == 3:
        printline()
        max2()
    elif choice == 4:
        printline()
        fibonacci()
    elif choice == 5:
        printline()
        num =int(input("Enter any Number : "))
        print(evenodd(num))
    elif choice == 6:
        printline()
        n = int(input("Enter total Numbers of Natural Number : "))
        if n>0:
            print("The Sum of Natural Numbers is : ",natural(n))
        else:
            print("Enter Valid Natural Number")
    elif choice==7:
        printline()
        status = False
    else:
        print("Enter Valid Input.")