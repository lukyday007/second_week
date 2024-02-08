# # ver 1 : 재귀함수
# def attach_paper(N):
#     if N == 1:
#         return 1
#     elif N == 2:
#         return 3
#     return attach_paper(N - 1) + 2 * attach_paper(N - 2)
#
# for tc in range(1, int(input())+ 1):
#     case = int(input())
#     case /= 10
#     ans = attach_paper(case)
#     print(f"#{tc} {ans}")


# ver 2 : List
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = N // 10
    deft = [1, 3]

    if a > 2:
        for i in range(2, a):
            deft.append((deft[i - 1] + 2 * deft[i - 2]))

    print(f'#{tc} {deft[a - 1]}')





