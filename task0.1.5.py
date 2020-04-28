#defining a program that checks prime or not
def prime(a):
    fact=0
    for i in range(1,a+1):
        if a%i==0:
            fact+=1
    if fact<=2:
        return True
    else:
        return False

print("Select between the following by entering apt number:")
print("1.print all the prime numbers between a to b.")
print("2.check if a number is prime or not")
#if the input is correct
try:
    opt=int(input())
    if opt==1:
        print("enter the numbers a and b")
        a,b=map(int,input().split())
        #checking each element in the range
        for j in range(a,b+1):
            if prime(j):
                #printing the primes
                print(j)
    elif opt==2:
        print("enter the number to be checked")
        f=int(input())
        if prime(f):
            print("It is prime")
        else:
            print("It is not prime")
    else:
        print("Please enter a valid option after running again")
#if the input is correct   
except ValueError:
    print("Please enter a valid option after running again")
    


