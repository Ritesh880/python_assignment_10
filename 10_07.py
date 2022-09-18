# 7. Write a python script to print first N even natural numbers in reverse order

n = int(input("enter value of n "))
for i in range(2*n, 1,-1):
    if i % 2 == 0:
        print(i)
