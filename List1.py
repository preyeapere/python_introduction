list1 = [7,8,4,5,2]
total=0
for i in list1:
    # print(i)
    total=total+i
   # print(total)
    if total>100:
        total=total*50
        print("i am okay" + str(total))
    else:
        total=total-2
        print("hurray" +str(total))    
       

