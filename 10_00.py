'''print all the character of a string but stop printing if 'r' 
appeared in the sequence if the character succesfully printrd 
then print message all the characters are processed  '''

x=input("enter a string")
for i in x:
    if i=='r':
        break
    print(i,end='')
    print()
else:
     print("all the character are processed")