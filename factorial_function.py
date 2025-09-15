# find the factorial of a number using function
def factorial(num):
    fact=1
    if num == 1 or num == 0:
        return fact
    else:
        fact= num*factorial(num-1)
        return fact
n=int(input("Enter the no to find factorial : "))
result=factorial(n)
print("factorial of",n,"is",result)


# with for loop
n=int(input("Enter the no to find factorial : "))
fact=1
for i in range(1,n+1):
    fact=fact*i

print("factorial of",n,"is",fact)