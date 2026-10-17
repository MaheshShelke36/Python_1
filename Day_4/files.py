#1.Write a program to read a file and count how many vowels are present in its content.
"""f= open("demo.txt", "r")
text=f.read()

vowels= "aeiouAEIOU"
count=0

for char in text:
    if char in vowels:
        count+= 1

print("total vowels: ",count)
f.close()        """

#2.Read all lines from a file into a list.print the total number of lines and display the 2nd and 4th line.
"""f=open("demo.txt","r")
lines= f.readlines()

print("Total lines: ", len(lines))

print("2nd line: ", lines[1])
print("4th line: ", lines[3])
f.close()"""

#3.take a sentence from the user,split it into words and store them in a list.print the longest word.

"""sen=input("enter a Sentence: ")

words= sen.split()

longest=words[0]
for word in words:
    if len(word)> len(longest):
        longest= word

print("longest word: ", longest)   """  

#4.	Read a file,spilt its content into words, and store them in a list
#  1.Print the total numbers of words
#  2.Print all the uiqiue words


f= open("demo.txt", "r")
content=f.read()

words= content.split()

print("total number of words: ", len(words))

unique_words= set(words)
print("unique words: ", unique_words)

f.close()