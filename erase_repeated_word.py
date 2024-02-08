# # ver 1 : append, pop 쓰기
# T = int(input())
#
# for tc in range(1, T+1):
#     arr = []
#     N = int(input())
#     for i in list(map(int, input().split())):
#         if i != 0:
#             arr.append(i)
#         else:
#             arr.pop()
#
#     print(f"#{tc} {sum(arr)}")

# ver 2 : 메서드 안쓰기
def pop(top):
    if top > -1:
        lst[top] = 0
        top -=1
    return top
def push(num, lst, top):
    top += 1
    if top < len(lst):
        lst[top] = num
    return top

T = int(input())
for tc in range(1, T + 1):
    top = -1
    N = int(input())
    arr = list(map(int, input().split()))
    lst = [0] * N
    for i in range(len(arr)):
        if arr[i] != 0:
            top = push(arr[i], lst, top)
        else:
            top = pop(top)
    print(f"#{tc} {sum(lst)}")














