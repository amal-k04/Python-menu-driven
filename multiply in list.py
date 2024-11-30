def multiply_list(m_list):
    product=1
    for i in m_list:
        product=product*i
    return product


m_list=[]
limit=int(input("no: of elements:"))
for n in range(limit):
    element=int(input("enter the element:"))
    m_list.append(element)
print("the product of elements in list is:",multiply_list(m_list))
