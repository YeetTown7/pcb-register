import sys
import os
import platform

def clear():
    if platform.system() == "Windows":
        os.system('cls')
        if "." in str(total):print(f"press 1 to add item; press 2 to clear; press 3 to checkout;  subtotal is ${total}")
        else:print(f"press 1 to add item; press 2 to clear; press 3 to checkout;  subtotal is ${int(total)}")
    else:
        os.system('clear')
        if "." in str(total):print(f"press 1 to add item; press 2 to clear; press 3 to checkout;  subtotal is ${total}")
        else:print(f"press 1 to add item; press 2 to clear; press 3 to checkout;  subtotal is ${int(total)}")

def clear_clean():
    if platform.system() == "Windows":
        os.system('cls')
        
    else:
        os.system('clear')
        

def wait():
    while True:
        break

total=0
orders=0
clear_clean()
print("welcome to the pcb register.")      
exit=input("press any key to continue.")
clear()
while True:
    choice=input("choose: ")
    if choice == "3":
        clear()
        print(f"subtotal: ${total}")
        print(f"tax: ${round(total*0.07,2)}")
        print(f"total: ${round(total*1.07,2)}")
        exit=input("press any key once paid.")
        clear()
        x=input("new order? (y/n) ")
        if x == "n": break
        total=0
        orders+=1
        clear()
    elif choice == "2": 
        clear()
        total=0
        print("cleared")
        exit=input("press any key to continue.")
        clear()
    elif choice == "1":
        clear()
        cost=round(float(input("price of item? $")), 2)
        total=total+cost 
        print("done")
        exit=input("press any key to continue.")
        clear()    
    else: 
        clear_clean()
        print("error")
        exit=input("press any key to continue.")
        clear_clean()
        break

orders+=1
print(f"you did {orders} order(s)")
exit=input("press any key to exit.")
clear_clean()
sys.exit()