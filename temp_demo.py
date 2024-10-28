'''
Author:Amal K Philip
Date:28-10-2024
Description:menu-driven Python program that allows users to convert temperatures
'''
while True:
    print("\t1.Celsius to Fahrenheit")
    print("\t2.Fahrenheit to Celsius")
    print("\t3.Exit")
    choice=int(input("Enter your choice:"))
    if choice==3:
        print("BYE BYEE")
        break
    elif choice==1:
        celsius=float(input("Enter the Celsius:"))
        fahrenheit=(celsius * 9/5) + 32
        print(f"Temperature in Fahrenheit is :{fahrenheit}")
    elif choice==2:
        fahrenheit=float(input("Enter the Fahrenheit:"))
        celsius=(fahrenheit - 32) * 5/9
        print(f"Temperature in Celsius is :{celsius}")
    else:
        print("INVALID ERROR")
