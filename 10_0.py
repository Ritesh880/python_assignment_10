# write a program to count 'a' in a given string using for loop
str = input("enter a string ")
count = 0
for x in str:
    if x == 'a':
        count += 1
      
print(count)