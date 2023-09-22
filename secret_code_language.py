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
        print("".join(i),end=" ")
    # print(l)


def decoding():
    s = input("Enter any Secret code Message : ").upper()
    new_s = s.split()
    l = []
    for i in new_s:
        i = list(i)
        if len(i) >= 3:
            # del i[0:3]
            # print(i)
            # input()
            # del i[-3:0]
            # print(i)
            # input()
            # i.pop(-1)    # how to remove last 3 element from list
            i = i[3:-3].copy()
            i.insert(0,i[-1])
            i.pop(-1)
            input()
        else:
            i.reverse()
        l.append(i)
        print("".join(i),end=" ")
        # print(l)
    # print(" ".join(l))
        


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












# st = input("Enter message")
# words = st.split(" ")
# coding = input("1 for Coding or 0 for Decoding")
# coding = True if (coding=="1") else False
# print(coding)
# if(coding):
#   nwords = []
#   for word in words:
#     if(len(word)>=3):
#       r1 = "dsf"
#       r2 = "jkr"
#       stnew = r1+ word[1:] + word[0] + r2
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))

# else:
#   nwords = []
#   for word in words:
#     if(len(word)>=3): 
#       stnew = word[3:-3]
#       stnew = stnew[-1] + stnew[:-1]
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))