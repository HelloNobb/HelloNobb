# hanoi top	> 개수만큼 A->C로 옮기기
def get_hanoi(n):
    if n == 1:
        return 1
    else:
        return 2*get_hanoi(n-1) + 1

N = int(input())
print(get_hanoi(N))