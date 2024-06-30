#i have have 50 in my account.people are adding money into my account and i want to see the value of money added
#while my account is still less than 1000
def new_value():
    i=10.3
    while i <500:
        print("enter the money")
        new_money=float(input())
        i=new_money+i
        print("this is the new balance " + str(i))
new_value()
        

    