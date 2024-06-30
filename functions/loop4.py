# write a python code that can loop through a list of items and collate the contents

listoffruit=["orange","apple","banana","pineapple","mango","pawpaw","grondnut"]
basket=[]
def list_item():
    for i in listoffruit:
        print("this are the items pickes " + i)
        basket.append(i)
        #print(basket)
list_item()
