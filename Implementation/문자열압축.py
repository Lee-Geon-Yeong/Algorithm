s=input()
sum=0
count=0
for i in range(len(s)//2):
    k=i+1
    for j in range(i, len(s), i):
        print(f"기준{s[0:i]} : 비교{s[k:j]}")
        k=j
        if s[0:i]==s[k:j]:
            count+=1
print(count)

# # len(s)//2
# abcabcabcabcdededdededede