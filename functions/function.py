Q_list=(1,4,8,13,15,26,18,19,23,25,34,56,79,90)
        
othervalues=[]
threshold=100


#Now it appears the specific numbers 15 and 34 appears in index 4 and 11 in the Q_list given
#write a funtion inside you have the two loops
for i in Q_list:
     if i==34:
          Final_outcome=i*threshold
          print(Final_outcome)
     else:
          othervalues.append(i)
          print(othervalues)
       

