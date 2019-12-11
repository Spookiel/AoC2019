p,q, r = list(map(int, input().split()))
n = int(input())
string = ""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
counter =1
import sys
def recurse(string, to_pick, possible, prev=1):
    global counter, start
    if to_pick==0:
        #print(string, counter)
        if counter==n:
            counter += 1
            print(string)
            print(time.time()-start)
            sys.exit(1)
            return
        counter += 1
        return

    for letter in possible:
        to_check = str(string)+letter
        if len(to_check)==1:
            cprev = 1
        elif letter==string[-1]:
            cprev = prev+1
        else:
            cprev = 1
        if cprev <= q:
            recurse(to_check, to_pick-1, possible, cprev)

possible = alphabet[:p]
import time
start = time.time()
recurse(string, r, possible)
print(time.time()-start)