"""n=[3,5,7,3,9,4,3,6,2]
freq=[0]*10

for i in n:
    freq[i]+=1
    print(freq[i])   """

def countFreq(n):
    freq=[0]*10

    while(n!=0):
        last_digit=n%10
        freq[last_digit]+=1
        n//=10

        return freq

n=1324678553

res=countFreq(n)

for i in range(len(res)):
    print(f"{i} -> {res[i]}")
    