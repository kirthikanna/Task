# You have been three lists. Your task is to find the duplicates in the three lists.
# Write a python program for the same. You can use your own python lists?
a=[1,2,3,4,5],[2,4,6,8,10],[2,4,7,9,11]
duplicate=[]
for sublist in a:
 for number in sublist:
     count=0
     for i in a:
         count += i.count(number)
     if count >1 and number not in duplicate:
         duplicate.append(number)
print(duplicate)


