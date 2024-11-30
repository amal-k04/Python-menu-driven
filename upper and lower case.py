def lower_upper(String):
    upper=0
    lower=0
    for i in String:
        if i.isupper():
            upper=upper+1
        if i.islower():
            lower=lower+1
    print('No. of Upper case characters :',upper)
    print("No. of lower case characters :",lower)
String=input("enter the string:")
lower_upper(String)