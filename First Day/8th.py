# num=int(input("Enter the Number:"))
# Sum=0
# while(num!=0):
#     digit=num%10
#     Sum=Sum+digit
#     num=num//10

# print(Sum)

num=int(input("Enter The Number:"))
sum=0
y=num
while(y!=0):
    digit=y%10
    sum=sum+digit*digit*digit
    y=y//10


if(sum==num):
    print("arm")
else:
    print("narm")
    
