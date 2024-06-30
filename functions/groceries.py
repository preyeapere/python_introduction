# Your wife has gone to the market to buy 3 items write a python code that will itemize 
# this items with their prices yam, stationeries and vegetable.
def groceries():
    print("enter your first item")
    first_item=input()
    print("enter the price of first item")
    first_item_price=float(input())
    print("enter your second item")
    second_item=input()
    print("enter the price of second item")
    second_item_price=float(input())
    print("enter your third item")
    third_item=input()
    print("enter the price of item")
    third_item_price=float(input())
    print("this is the total detail of groceries " + first_item + ":" + str(first_item_price) + "," + second_item + ":" + str(second_item_price) + "," + third_item + ":" + str(third_item_price))

groceries()