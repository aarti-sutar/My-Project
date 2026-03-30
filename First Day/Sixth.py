#123--->3
#12345-->5
num=int(input("Enter the Number:"))

c=0
while(num>0):
    num//=10
    c+=1

print("no of digit in given number:",c)

#123--->321

num=int(input("Enter the number:"))
rev=0

while(num>0):
    digit=num%10
    rev=rev*10+digit
    num//=10
print("Reverse number=",rev)


