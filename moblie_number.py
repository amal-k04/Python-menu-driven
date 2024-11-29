"""
Author:Aml k philip
Date:29-11-2024
Description:Program to check whether the given number is a valid mobile number or not.
"""


def mobi_number(mobile_no):
    if len(mobile_no)==10:
        if mobile_no[0]=="7":
            print(" The given mobile number is VALID")
        elif mobile_no[0]=='8':
            print(" The given mobile number is VALID")
        elif mobile_no[0]=='9':
            print(" The given mobile number is VALID")
        else:
            print("NOT VAILD")
    else:
        print("NUMBER SHOULD CONTAIN 10 DIGIT")



mobile_no=(input("Enter the mobile number:"))
mobi_number(mobile_no)