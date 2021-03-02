N=int(input())
T=[]
P=[]
answer=[0]*10000
for i in range(N):
    a, b=map(int, input().split())
    T.append(a)
    P.append(b)

for day in range(N):
    
    answer[T[day]]=max(P[day]+P[T[day]], answer[T[day]])

print(answer)



