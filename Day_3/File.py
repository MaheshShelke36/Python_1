#file operation
#read file

f= open("myfile1.txt")
print(f.read())

f.close()

#using with a option no need to close file exclusively

with open("myfile1.txt") as f:
    print(f.read(6))
    ct=f.read()
    ws=ct.spilt()
    print("total characters :- ",len(ct))
    print("total words ", len(ws))

#line by line reading
with open("myfile.txt") as f:
    l1=f.readline() 
    l2=f.readline()
print("first line :-",l1, "second line :-",l2)  

#reading file without readline

with open("myfile1.txt") as f:
    print("output using for")
    for i in f:
        print(i)

with open("myfile.txt","r") as f:
    print("\noutput using readlines which read complete file")
    txt=f.readline()
f.close()

#

with open("myfile1.txt", "r")as f:
    f.write("\n newly added contents in div B")

    #after adding on eline
with open("myfile1.txt","r")as f:
    print(f)    

#overwrite
    
with open("myfile.txt","w")as f:
    f.write("new file created ")
f.read()        