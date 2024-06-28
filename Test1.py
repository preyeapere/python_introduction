animals ="pig,cat,goat"
pictures =""
int_price =100
new_price =0
price =0
New_Number=0
while pictures != animals:
    print("enter your pictures item")
    pictures =input()

    if pictures == animals:
        print("hurray you are correct")
        print("please tell me the total price")
        price=int(input())
        
        new_price=int_price+price
        print(new_price)
        new_price=new_price*30
        print("This is the new price" + str(new_price))
        
    else:
        print("you are wrong please try again")
        New_Number=3+5
        print(New_Number)
        New_Number= (New_Number*50)-20
        print("This is my New Number" + str(New_Number))



