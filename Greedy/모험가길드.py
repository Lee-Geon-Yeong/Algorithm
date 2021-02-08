N=int(input())
data=list(map(int, input().split()))
data.sort()
count=0
last=len(data)-1
while():
    for i in range(data[last-1]):
        del(data[i])

    last-=1
    count+=1

print(data)
print(count)
