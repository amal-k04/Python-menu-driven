def factorial(n):
    if n==0:
        return 1
    else:
        return (n*factorial(n-1))

n=int(input("Enter the number:"))
if n>0:
    print("the factorial of",n,"is",factorial(n))
else:
    print("PLEASE ENTER A POSITIVE NUMBER:")