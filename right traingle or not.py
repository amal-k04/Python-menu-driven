"""
Author:Amal k philip
Date:29-11-2024
Description:A program that accepts the lengths of three sides of a triangle as inputs. The program should output whether or not the triangle is a right triangle 
"""
def right_triangle():
    if list_triangle[2]**2==list_triangle[0]**2+list_triangle[1]**2 :
        print("the given triangle is a right triangle")
    else:
        print("the given triangle is not a right triangle")

side1=int(input("Enter the length of the first side:"))
side2=int(input("Enter the length of the Second side:"))
side3=int(input("Enter the length of the Third side:"))
list_triangle=[side1,side2,side3]
list_triangle.sort()
right_triangle()