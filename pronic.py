import math
n = int(input("enter a number to check"))
x = int(math.sqrt(n))
if(x*(x+1)==n):
    print("It is a pronic number")
else:
    print("Not a pronic number")