test = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""

data = """292, 73
204, 176
106, 197
155, 265
195, 59
185, 136
54, 82
209, 149
298, 209
274, 157
349, 196
168, 353
193, 129
94, 137
177, 143
196, 357
272, 312
351, 340
253, 115
109, 183
252, 232
193, 258
242, 151
220, 345
336, 348
196, 203
122, 245
265, 189
124, 57
276, 204
309, 125
46, 324
345, 228
251, 134
231, 117
88, 112
256, 229
49, 201
142, 108
150, 337
134, 109
288, 67
297, 231
310, 131
208, 255
246, 132
232, 45
356, 93
356, 207
83, 97"""

from collections import defaultdict


def dist(coord1, coord2):
    return abs(coord1[0]-coord2[0])+abs(coord1[1]-coord2[1])


def is_infinite(board, bound):
    #(k[0]==c and k[1]==0) or (k[0]==c and k[1]==bound-1) or (k[1]==c and k[0]==0) or (k[0]==bound-1 and k[1]==c)
    found = set()
    for k in board.keys():
        if ((0 <= k[0] < bound) and (k[1]==0 or k[1]==bound-1)) or ((0 <= k[1] < bound) and (k[0]==0 or k[0]==bound-1)):
            for j in board[k]:
                found.add(j)
    return found


def run(data, bound=10):
    board = defaultdict(set)
    coords = [list(map(int, i.split(", "))) for i in data.splitlines()]
    for y in range(bound):
        print(y)
        for x in range(bound):
            points = [dist(i, (x, y)) for i in coords]
            d2 = [i for i in coords if dist(i, (x, y))==min(points)]
            if len(d2) > 1:
                board[(x, y)] = set()
            else:
                board[(x, y)] = set(map(tuple, d2))
    to_check = {tuple(i):0 for i in coords if tuple(i) not in is_infinite(board, bound)}
    for k, v in board.items():
        for a in v:
            if a in to_check.keys():
                to_check[a] += 1
    print(max(to_check.values()))

run(test)
run(data, 360)