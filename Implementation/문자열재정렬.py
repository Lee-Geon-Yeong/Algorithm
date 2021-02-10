S=list(input())
S.sort()
sum=0
for i in range(len(S)):
    if int(ord(S[i]))-int(ord("A"))+1<0:
        sum+=int(S[i])
    else:
        continue
        
print(S)
print(''.join(S)+str(sum))

