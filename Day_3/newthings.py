#sample string
text="Mahesh"

#title case(capitlize each other)
print(text.title())

#count occurrence of a substring
print("Letter c occurs ", text.count("c"),"times in text")

#find the position of a substring (-1 if not found)
print("position of imcc")

#join a list of string with seprator
words=["Python","is","fun"]
print("".join(words))

#parition a string into 3 parts(before,seperator,after)
print(text.partition("come"))

#expand tabs to space



#empty list
my_list=[]
print(my_list)

#to access list element use index
#psotive numbers indicate from stsart negative numbers
#0 is first element and -1 is alst element

numbers=[10,20,30,40]
print(numbers[0])
print(numbers[-2])

#append item list
colors=["red","blue"]
colors.append("green")
print("after adding at last ",colors)

#insert at specific location
colors.insert(1,"yellow")
print("after insertion at second position",colors)

#remove
print("before remove",colors)
colors.remove("red")
print("after removal of red",colors)
#pop removes last item

last_color=colors.pop()
print(last_color)
print("after pop operation",colors)

#length
num=[1,2,3,4,5,6]
print("no,of")
#sum
print("sum of the list number is ",sum(numbers))

#sorting
print("list in asending order ",sorted(numbers))
print("list in desending order ",sorted(numbers, reverse=True))

#blocks
if True:
    print("inside blocks")
print("outside blocks")

# if statement -> executes if condition is true
# else statement

x=int(input("enter value"))
if x>0:
    print("positive")
elif x==0:
    print("zero")
else:
    print("negative")

#while loop
print("output of while loop")
count=0
while count<5:
    print(count)
    count += 1

#for loop
print("prints numbers using for loop")
for i in range(5):
    print(i)

#loop control keywords

for i in range(5):
    pass

#conitue skips current iteration
print("output of for loop")
for i in range(5):
    if i==2:
        continue
    print(i)

#loop else
print("output of for loop with else")
for i in range(3):
    print(i)
else:
    print("loop finished wothout break")

 #create dictionary with student details
 students={
       101:{"name": "aditi","scores": [70,80,67]},
       102:{"name": "rahul","scores": [89,44,33]},
 }

#calculate the aveg score and flag pass/fail
for sid,details in students.items():
    avg=sum(details["Scores"])/ len(details["Scores"])
    details["Average"]= avg
    details["Passed"]=avg>=50 #boolean flag

#print names of student who passed
print("students who passed:")
for sid,details in students,items():
    if details["Passed"]:
        print(details["name"])


      
