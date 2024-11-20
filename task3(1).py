# create two list one which all have even numbers and another list which all have odd numbers
#in it.


list=[10,501,22,37,100,999,87,351]
list_of_even=[]
list_of_odd=[]
for i in list:#iterates over each element i in the input list
    if i%2==0:#check if i is even by using %(modulo operator) if rem is 0, i is even
        list_of_even.append(i)#if i is even add it to the list_of_even
    else:
        list_of_odd.append(i)
print("list: ", list)
print("list_of_even: ",list_of_even)
print("list_of_odd: ",list_of_odd)