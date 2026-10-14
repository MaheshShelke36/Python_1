"""text="welcome to imcc"
print("let a occurs in ",text.count("a"),"words in te")"""

"""words=["vaibhav ""likes","pranika"]
print("".join(words))"""

#find out the max and min element in a list
"""num=[10,20,30,40,50,60]
maximum=max(num)
minimum=min(num)
print("Maximum: ",maximum)
print("Minimum: ",minimum)"""

#insert a item at 6 position this number must be 1/3 of number stored at fourth position
"""num=[10,20,30,40,50,60]
item=num[4]//3
num.insert(5,item)
print(num)"""

#create a list of 10 num print the sum of last 4 elements of the list
"""my_list=[10,20,30,40,50,60]
print("sum of last 4 numbers",sum(my_list[-4:]))"""

#create Dictionary and show result
"""students={
       101:{"name": "aditi","scores": [70,80,67]},
       102:{"name": "rahul","scores": [89,44,33]},
       103:{"name": "Sahil", "scores":[50,60,70]}
 }

for sid,details in students.items():
    avg=sum(details["scores"])/len(details["scores"])
    details["Average"]= avg
    details["Passed"]=avg>=50 

print("students who passed:")
for sid,details in students.items():
    if details["Passed"]:
        print(details["name"])"""

#wap to guees number

"""num=7
guess=int(input("guess the number between 1 to 10: "))

if guess == num:
    print("Correct")
else:
    print("Wrong!")"""

#wap to replace voewls with z

"""name=input("Enter your name:")
result=""
for ch in name:
    if ch in "aeiouAEIOU":
        result=result + "z"
    else:
        result=result + ch
print("Result:",result)"""

#create a list of number and string acceot the values from user.seperate the list from the maximum number
#dispay the names desinding orde
names=[]
numbers=[]

create=input("Enter a number or name")

for i in range(create):
    name=input("Enter the name: ")
    num=int(input("Enter the number: "))

    names.append(name)
    numbers.append(num)

data=list(zip(numbers,names))

data.sort(reverse=True)

print("\n Names in descending order: ")
for num,name in data:
    print(name,num)