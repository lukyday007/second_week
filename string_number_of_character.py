# # 문자열_글자수
#
# T = int(input())
# for tc in range(1, T+1):
#
#     aStr = input()
#     bStr = input()
#     aDict = {}
#     for a in aStr:
#         aDict[a] = aDict.get(a, 0)
#     for b in bStr:
#         if b in aDict:
#             aDict[b] += 1
#
#     aDict = dict(sorted(aDict.items(), key=lambda item: item[1], reverse = True))
#
#     value = list(aDict.values())
#     print(f"#{tc} {value[0]}")

# # 문자열_문자열 비교_확인용
# T = int(input())
# for tc in range(1, T+1):
#     a = input()
#     b = input()
#     result = 0
#     if a in b:
#         result = 1
#     else:
#         result = 0
#     print(f"#{tc} {result}")

# 문자열 교환하기
s = list('algorithm')
N = len(s)

for i in range(N//2):
    s[i], s[N-1-i] = s[N-1-i], s[i]

print(" ".join(s))

# # 초심자의 회문 검사
# # ver 1
# T = int(input())
# for tc in range(1, T+1):
#     test = input()
#     testList = list(test)
#
#     result = True
#     while len(testList) > 0:
#         if len(testList) == 1 :
#             break
#         if testList.pop(0) == testList.pop():
#             result = True
#         else:
#             result = False
#
#     if result == True:
#         print(f"#{tc} 1")
#     else:
#         print(f"#{tc} 0")
#
# # ver 2
# T = int(input())
# for tc in range(1, T + 1):
#     str1 = input()
#
#     if str1 == str1[::-1]:
#         print(f'#{tc} 1')
#     else:
#         print(f'#{tc} 0')

def change(cha):
    if cha == "b":
        return "d"
    if cha == "d":
        return "b"
    if cha == "p":
        return "q"
    if cha == "q":
        return "p"

T = int(input())
for tc in range(1, T+1):
    test = input()
    testList = list(test)

    tmpStr = ""
    for t in testList[::-1]:
        change(t)
        tmpStr += change(t)
    print(f"#{tc} {tmpStr}")






