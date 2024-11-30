def sum_list(s_list):
    sum=0
    for i in s_list:
        sum=sum+i
    return sum

s_list=[]
limit=int(input("no: of elements:"))
for n in range(limit):
    element=int(input("enter the element:"))
    s_list.append(element)
print("the sum of elements in list is:",sum_list(s_list))