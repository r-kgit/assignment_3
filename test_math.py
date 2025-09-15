# test math module

import math

# value of pi
print(math.pi)
# find the square root
n=int(input("Enter the no to find sqrt : "))
print("square root of " ,n," is ",math.sqrt(n))

# find the log of given value
x=int(input("Enter the no to calculate log : "))
b=int(input("Enter base : "))
print("log of " ,x," on base ",b ," is ",math.log(x,b))

#find the sin of any given angle
d=float(input("Enter the no to find sin  in degree: "))
r = math.radians(d)
print("sin of " ,d," is ", math.sin(r))

