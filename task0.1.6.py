#a function that generates n fibonacci terms list
def fibonacci(n):
    # return a list of fibonacci numbers
    a=0
    b=1
    c=0
    l=[]
    for _ in range(n):
        l.append(c)
        a=b
        b=c
        c=a+b
    return l

print("Select between the following by entering apt number:")
print("1.print all the fibonacci series less than a given number.")
print("2.check if a number is in fibonacci series")
print("3.print n terms of fibonacci series")
#taking input option
opt=input()
#for option 1
if opt=='1':
    print("enter the number less than which fibonacci series is to be displayed")
    n=int(input())
    #generating a list of fibonacci that has to have numbers greater than n
    lis=fibonacci(n+2)
    print("printing fibonacci series upto the number")
    #we only need fibonacci elements upto n
    for j in lis:
        if j<=n:
   			#printing the result
            print(j,end=" ")
elif opt=='2':
    print("enter the number to be checked")
    n=int(input())
    #generating a list of fibonacci that has to have numbers greater than n
    lis=fibonacci(n+2)
    #checking for presence of n as fibonacci element
    if n in lis:
        print("Yes it occurs in fibonacci series")
    else:
        print("No the number doesn't occur in fibonacci series")
elif opt=='3':
    print("enter the number of terms of fibonacci series")
    #taking input and simultaneously generating the list of fibonacci upto the number
    for i in fibonacci(int(input())):
        print(i,end=" ")
else:
    print('enter a valid option after running again')
    



