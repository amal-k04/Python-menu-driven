def range_num(num):
    if num in range(lower,upper+1):
        print("the given number is in the range")
    else:
        print("the given number is NOT in the range")


lower=int(input("enter the lower limit:"))
upper=int(input("enter the upper limit:"))
num=int(input("enter the upper limit:"))
range_num(num)