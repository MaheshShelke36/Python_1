# sent=input("Enter a sentence: ")

# count=0
# for ch in sent:
#     if ch in "aieouAIEOU":
#         count= count+1
# print("number of vowels= ",count)        


list   = ["a","c","b","a","c","b","a"]


for i in range(len(list) -1 , -1,-1):
    for j in range(i -1, -1,-1):
        if(list[i] == list[j]):
            list.pop(j)
            break
print(list)