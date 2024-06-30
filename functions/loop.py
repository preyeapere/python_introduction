#write and python function that will loop through the following list of numbers 30,90,70,21,40,200,101
# write a python function that will loop through this number and get all the numbers that are greater
#than 40
m=[]
list=[30,90,70,21,40,200,101]
def new_number():
 
    for i in list:
        if i>40:
            m.append(i)
            print("I just added this number " + str(i))
new_number()

            
    