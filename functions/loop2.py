#write and python function that will loop through the following list of numbers 30,90,70,21,40,200,101
# write a python function that will loop through this number and get all the numbers that are greater
#than 70
basket=[]
new_account=0
list=[30,90,70,21,40,200,201]
def new_basket():
    for i in list:
        if i>70:
            basket.append(i)
            print("i just added a number " + str(i))
            new_account=i*1000
            print("this is the current value " + str(new_account))
new_basket()
