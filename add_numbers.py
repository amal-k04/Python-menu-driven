def add_no(num_1,num_2):
    if num_2==0:
        return num_1
    else:
        return add_no(num_1+1,num_2-1)

num_1=int(input("Enter the first number:"))
num_2=int(input("Enter the second number:"))
print("the sum of",num_1,'&',num_2,"is",add_no(num_1,num_2))