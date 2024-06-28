
item_list = ['item', 5, 'foo', 3.14, True]
for i in item_list:
    print(i)
    if i=="foo":
        item_list.remove(i)

        print("i removed foo")
        print(item_list)
        break
