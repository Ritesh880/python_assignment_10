#4. Write a python script to print first N odd natural numbers

n=int(input("enter value of n "))
for i in range(0,2*n):
    if i%2!=0:
       print(i)