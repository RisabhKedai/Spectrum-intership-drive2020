#Accept string from a user and display only those characters which are present at an even index number
st=input("Please enter your string \n")
#to print even index characters start from 0
ini=0
#iterating through every even index and printng result
print("the even index characters are")
while ini<len(st):
	print(st[ini],end=" ")
	ini+=2


