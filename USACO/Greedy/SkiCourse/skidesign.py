"""
ID: luke.mo1
LANG: PYTHON3
TASK: skidesign
"""

with open("skidesign.in", "r") as f:
    n = int(f.readline())
    lines = [(int(f.readline()), False) for _ in range(n)]


total = 0
lines = sorted(lines)
while lines[-1][0]-lines[0][0] > 17:
    diff = lines[-1]-lines[0]-17
    print(diff, lines[-1],lines[0])
    if diff%2==0:
        total += 2 * ((diff // 2) ** 2)
        lines[0] += (diff // 2)
        lines[-1] -= (diff // 2)
    else:
        total += (diff // 2) ** 2
        total += ((diff // 2) + 1) ** 2
        lines[0] += (diff // 2)
        lines[-1] -= (diff // 2) + 1
    lines = sorted(lines)

print(lines)
with open("skidesign.out", "w+") as f:
    f.write(str(total)+"\n")