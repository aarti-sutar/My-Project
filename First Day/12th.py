#Loop in dictionary
student={
    "name": "AS",
    "age" : 20
}

for key in student:
 print(key,student[key])

for k,v in student.items():
 print(k,"=",v)

#Loop in set

s={10,20,20}
for x in s:
 print(x)
