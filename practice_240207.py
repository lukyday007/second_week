# # 참고 스택의 구현
# def push( item, size ):
#     global top
#     top += 1
#     if top == size:
#         print('overflow!')
#     else:
#         stack[top] = item
#
# size = 10
# stack = [0] * size
# top = -1
#
# push(10, size)
# top += 1
# stack[top] = 20  # push(20, size)
# print(stack)


# def pop ( ):
#     global top
#     if top == -1:
#         print('underflow')
#         return 0
#     else:
#         top -= 1
#         return stack[top + 1]
# print(pop())
#
# stack = [0]
#
# if top > -1:    # pop( )
#     top -= 1
#     print(stack[top + 1])

# def push(n):
#     global top
#     top += 1
#     if top == size:
#         print('Overflow!')
#     else:
#         stack[top] = n
#
#
# top = -1
# size = 10
# stack = [0] * size
#
# top += 1            # push(10)
# stack[top] = 10
#
# top += 1
# stack[top] = 20     # push(20)
#
# push(30)
#
# while top >= 0:
#     top -= 1
#     print(stack[top + 1])

# def f2(n):
#     n *= 2
#     print(n)
#
# def f1(c, d):
#     e = c + d
#     f2(e)
#
# a = 10
# b = 20
# c = a + b
# f1(a, b)

#
# def fibo(n):
#     # Base cases
#     if n < 2:
#         return n
#     else:
#         # Recursive call
#         return fibo(n - 1) + fibo(n - 2)
#
# def fibo1(n, memo):
#     # Use memo to check if fibo1(n) is already computed
#     if memo[n] is not None:
#         return memo[n]
#     if n < 2:
#         memo[n] = n
#     else:
#         memo[n] = fibo1(n-1, memo) + fibo1(n-2, memo)
#     return memo[n]
#
# # Initialize the memoization array
# def initialize_memo(n):
#     memo = [None] * (n + 1)
#     memo[0], memo[1] = 0, 1
#     return memo
#
# # Example usage:
# n = 10  # Example value for n
# memo = initialize_memo(n)  # Initialize the memoization array
# print(fibo1(n, memo))  # Calculate the nth Fibonacci number using memoization
# print(memo)



















