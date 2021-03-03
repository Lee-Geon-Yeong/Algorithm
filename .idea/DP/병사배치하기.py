# 병사 배치하기
# '가장 긴 감소하는 부분 수열' 구하기 문제

n = int(input())
sd = list(map(int, input().split()))

arr = [1]*n   # n>=1 조건이므로 1로 초기화 
sd.reverse()   # 역순 -> '가장 긴 증가하는 부분 수열' 문제로 변경

# LIS / 가장 긴 증가하는 부분수열 구하기
for i in range(1,n):
    for j in range(i):
        # 최대 길이를 갱신
        if sd[j] < sd[i]:
            # arr[j]+1 : if에서 증가함을 확인했기 때문에 이전의 최댓값 arr[j]에 1을 더함
            arr[i] = max(arr[i], arr[j]+1)
        print('i:', i, 'j:',j)
        print(arr)
# 전체 길이에서 값이 증가한 길이를 빼줌
print(n-max(arr))