#remove the duplicates from the list

lst=[1,2,4,4,6,6,7,8]
new_list=[]

for i in lst:
    if i not in new_list:
        new_list.append(i)
print(new_list)        