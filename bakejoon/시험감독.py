def solution():
    n = int(input())
    people = list(map(int, input().split()))
    b, c = list(map(int, input().split()))

    ans = n
    for i in range(n):
        remain = people[i] - b
        if remain <= 0:
            continue
        if remain % c == 0:
            ans += (remain // c)
        else:
            ans += (remain // c + 1)
    
    print(ans)

solution()