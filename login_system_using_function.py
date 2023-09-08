db = {}

def registration(name,email,password):
    db['name'] = name
    db['email'] = email
    db['password'] = password
    return 'registration successfully'
def login(email,password):
    if email == db['email']:
        if password == db['password']:
            return f'welcome  {db["name"]}'
        else:
            return 'Invalid Password'
    else:
        return 'Invalid Email'
    
status = True
while status:
    menu = '''
                                    Welcome
       
         Press 1 for Registration                Press 2 for Login
                          
                           press any other key to EXIT

'''
    print(menu)
    choice = (input("Enter your Choice : "))
    if choice  == '1':
        name = input("Enter your Name : ").title()
        email = input("Enter your Email : ")
        password = input("Enter your Password : ")
        print(registration(name,email,password))
    elif choice == '2':
        email = input("Enter your Email : ")
        password = input("Enter your Password : ")
        print(login(email,password))
    else:
        status=False
        print("Thak you for using our Application")