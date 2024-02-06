T = 0
for tc in range(1, T+1):
    N = int(input())
    string = input()
    sentence = input()
    cnt = 0

    for i in range(len(sentence) - len(string) + 1):
        if sentence[i:i+len(string)] == string:
            cnt += 1

    print(f"#{tc} {cnt}")