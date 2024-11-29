def GCD(num1,num2):
    if num2==0:
        return num1
    else:
        num3=num1%num2
        num1=num2
        num2=num3
        return GCD(num1,num2)
num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
print("GCD is:",GCD(num1,num2))