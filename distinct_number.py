def distinct(m_list):
    main_list=[]
    for i in m_list:
        if i not in main_list:
            main_list.append(i)
        else:
            continue
    print(main_list)


m_list=[]
limit=int(input("no: of elements:"))
for n in range(limit):
    element=int(input("enter the element:"))
    m_list.append(element)
distinct(m_list)