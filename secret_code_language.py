import random
import string
def encode():
    s = input("Enter any message : ").upper()
    new_s = s.split()
    l = []
    for i in new_s:
        rand_char = []
        i = list(i)
        if len(i) >= 3:
            i.append(i[0])
            i.remove(i[0])
            for n in range(0,6):
                a = random.choice(string.ascii_uppercase)
                rand_char.append(a)
            i.extend(rand_char)
            rand_char
            for j in range(0,3):
                i.insert(0,i[-1])  
                i.pop()
        else:
            i.reverse()
        l.append(i)
    print(l)
def decoding():
    s = input("Enter any Secret code Message : ").upper()
    new_s = s.split()
    l = []
    for i in new_s:
        i = list(i)
        if len(i) >= 3:
            del i[0:3]
            del i[-3:-1]
            i.pop(-1)    # how to remove last 3 element from list
            i.insert(0,i[-1])
            i.pop(-1)
            print(i)
        else:
            i.reverse()
        l.append(i)
        


status = True
menu = """

                Please select anyone option from below 

    press 1 for Decoding                   press 2 for Encoding

                      press any key for exit
"""
while status:
    print(menu)
    choice = int(input("Enter your choice : "))
    if choice == 1:
        decoding()
    elif choice == 2:
        encode()
    else:
        status = False