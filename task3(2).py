#Given a Python List [10,501,22,37,100,999,87,351] your task is to Count all the Prime Numbers and
# create a new Python List which will contain all the Prime Numbers in it
list =[10,501,22,37,100,999,87,351]
list1=[]
for i in list:
    if i>1:#prime numbers are greater than 1
        for j in range(2,int(i**0.5),+1):
            if i%j==0:#if divisible,not prime
                break
        else:#if no divisors ,prime
                list1.append(i)
print("Prime numbers:", list1)
