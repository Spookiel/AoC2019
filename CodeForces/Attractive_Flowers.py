n = int(input())
flowers = list(map(int, input().split()))
total = 0
if n%2==1:
    for i in flowers:
        if i%2==0:
            total += i-1
        else:
            total += i
    print(total)
else:
    for i in flowers:
        if i%2==0:
