def max_number(num2,num3):
    if num2<num3:
        return num3
    else:
        return num2
def max_three(num1,max_two):
    if num1<max_two:
        return max_two
    else:
        return num1



num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
max_two=max_number(num2,num3)
print(max_three())