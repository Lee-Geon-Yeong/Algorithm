# n=int(input())
# frame=[]
# for _ in range(n):
#     frame.append(list(map(int,input().split())))
n=5
frame=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

for i in range(1,n):
    for j in range(i+1):
        #왼쪽에서 내려옴
        if j==0:
            up_left=0
        else:
            up_left=frame[i-1][j-1]
        #바로 위에서 내려옴
        if j==i:
            up=0
        else:
            up=frame[i-1][j]
        print('up_left=%d, up=%d, 처음frame[%d][%d]=%d'%(up_left,up,i,j,frame[i][j]))
        frame[i][j]=frame[i][j]+max(up_left,up)
        print('i=%d j=%d 이후frame[%d][%d]=%d'%(i,j,i,j,frame[i][j]))
        print('-'*50)
print(max(frame[n-1]))