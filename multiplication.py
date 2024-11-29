


def multiply(num1,num2):
    if num2==1:
        return num1
    else:
        return num1+0multiply(num1,num2-1)

num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
print("the product of",num1,"&",num2,"is",multiply(num1,num2))