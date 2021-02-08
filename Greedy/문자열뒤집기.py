data=list(map(int, input()))
zero=data.count(0)
one=data.count(1)

count=0
if zero>=one:
    for i in data:
        if i==1:
            count+=1

