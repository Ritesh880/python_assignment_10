# 5. Write a python script to print first N odd natural numbers in reverse order

n = int(input("enter number "))
for i in range(2*n, 0, -1):
    if i % 2 != 0:
        print(i)
