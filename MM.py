from math import sqrt
number = int(input("Enter your number"))
if number  > 1:
  for x in range(2, int(sqrt(number)) + 1):
    if (number %x) == 0:
       print("That is not a prime number")
       break
    else:
       print("This is a prime number")
else:
   print("This is not a prime number")
