'''
Author:Amal K Philip
Date:28-10-2024
Description:menu-driven Python program that allows users to convert temperatures
'''
balance_amount=10000
while True:
    print("\t1.Check Balance")
    print("\t2.Deposit Money")
    print("\t2.Withdraw Money")
    print("\t4.Exit")
    choice=(input("enter your choice:"))
    if choice=="4":
        print("THANK YOU")
        break
    elif choice=='1':
        print(f"CURRENT BALANCE: ${balance_amount}")
    elif choice=="2":
        dep_money=float(input("Enter the Amount"))
        balance_amount=balance_amount+dep_money
        print(f"The ")
        print(f"The Deposit Amount ${dep_money} \n"
              f"The Current Amount ${balance_amount}")
    elif choice=='3':
        withdraw_Amount=float(input("The Amount to be withdraw:"))
        balance_amount=balance_amount-withdraw_Amount
        if (withdraw_Amount>balance_amount):
            print("INSUFFICIENT AMOUNT")
        else:
            print(f"WITHDRAW AMOUNT ${withdraw_Amount}\n"
              f"CURRENT BALANCE 4{balance_amount}")
    else:
        print("INVALID ERROR")