# Given a Python List [10,501,22,37,100,999,87,351]
# Find out how many numbers are there in the given Python List which are Happy numbers?
a = [10,501,22,37,100,999,87,351]
b = []
def happy(a):#Defines the happy function taking list a as input.
    for i in range(len(a)):
#Initializes sum with the current number and enters a loop that
# continues until sum becomes 1 (happy) or 4 (unhappy).
        sum= a[i]
        while sum!=1 and sum !=4:
            tempsum=0
            for digit in str(sum):#converts the sum to string.
                tempsum +=int(digit)**2#Converts digit back to integer, squares it, and adds to tempsum
                sum = tempsum
            if sum ==1:
             b.append(a[i])
            return b
print(happy(a))