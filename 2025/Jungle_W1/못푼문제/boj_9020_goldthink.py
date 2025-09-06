#골드바흐 - 2제외 모든 짝수는 두 소수의 합으로 나타낼 수 있음

## 일단 <에라토스테네스의 체> 이용해 소거법으로 100까지만 소수구하기
PRIMES = [] # 1만까지의 전체 소수 집어넣음
count=0
for num in range(2, 10000):
    idx=-1
    # num 소수판별
    for i in range(2,num+1):
        if num % i == 0:
            idx = i
            break
    if idx == num: #소수조건
       count+=1
       PRIMES.append(idx)



# N = int(input()) #2
# nums = [int(input()) for _ in range(N)] # 8 16
# nums = nums[:N]