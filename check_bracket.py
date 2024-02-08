# ver 1
# T = int(input())
# for tc in range(1, T+1):
#     string = input()
#     brackets = ['(', '{', '[' , ']', '}', ')']
#     strList = list(string)
#     check = []
#     result = 0
#     for b in strList:
#         if b in brackets:
#             check.append(b)
#     left = 0
#     right = 0
#     for i in range(len(check)):
#         if check[i] == '(' or check[i] == '{' or check[i] == '[':
#             left += 1
#         if check[i] == ')' or check[i] == '}' or check[i] == ']':
#             right += 1
#
#     if left == right :
#         result = 1
#     else:
#         result = 0
#
#     print(f"#{tc} {result}")


# # ver 2
# T = int(input())
# for tc in range(1, T+1):
#     string = input()
#     bra = ['(', '{', '}', ')']
#     brackets = ['(', '{']
#     strList = list(string)
#     check = []
#     stack = []
#     result = 0
#     for i in strList:
#         if i in bra:
#             check.append(i)
#
#     for b in check:
#         if b in brackets:
#             if b == "(" or b == "{":
#                 stack.append(b)
#
#         if b == ")":
#             if stack[-1] =="(":
#                 stack.pop()
#         if b == "}":
#             if stack[-1] == "{":
#                 stack.pop()
#     if len(stack) != 0:
#         result = 0
#     else:
#         result = 1
#
#     print(f"#{tc} {result}")

def push(item):
    global top
    top += 1
    stack[top] = item

def pop():
    global top
    stack[top] = 0
    top -= 1

for tc in range(1, int(input())+1):
    strList = list(input())
    stack = [0] * len(strList)

    result = 1
    top = -1

    for s in strList:
        if s == '(' or s == '{':
            push(s)
        elif s == ')':
            if stack[top] == '(':
                pop()
        elif s == '}':
            if stack[top] == '{':
                pop()
    for st in stack:
        if st != 0:
            result = 0

    print(f"#{tc} {result}")


# # ver by teacher
# T = int(input())
# for tc in range(1, T+1):
#     arr = input()
#     s = []
#     for ch in arr:
#         if ch == '(' or ch == '{':
#             s.append(ch)
#         elif ch == ')' or ch == '}':
#             if not s:
#                 break
#             val = s.pop()
#
#             if ch == ')' and val != '(':
#                 ans = 0
#                 break
#
#             elif ch == '}' and val != '{':
#                 ans = 0
#                 break
#     if s:
#         ans = 0
#     print(ans)







