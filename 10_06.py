#6. Write a python script to print first N even natural numbers

n=int(input("enter value of n "))
for i in range(1,2*n+2):
    if i%2==0:
        print(i)