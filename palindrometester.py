import math

value = input("Enter a word or phrase: ")
IsItAPalindrome = 0
mid = (math.floor(len(value)/2))

for i in range(0,mid):
    if(value[i] !=  value[(len(value)-1-i)]):
        IsItAPalindrome = 1 
if IsItAPalindrome   == 1:
    print("It's not a palindrome")
else:
    print("It's a palindrome")
    KeepGoing = input("Would you like to test another: (y,n) ")
    if len(KeepGoing) > 0 and KeepGoing[0].lower() == 'y':
        KeepGoing = 'y'

print("Ok, goodbye !!! ")



#if :

  #  else 