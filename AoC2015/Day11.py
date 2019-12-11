password = "cqjxjnds"
import itertools
import re
alpha = "abcdefghijklmnopqrstuvwxyz"
patterns = [alpha[i:i+3] for i in range(len(alpha))]
pattern = r"(.)\1"
print(len(list(itertools.permutations(alpha, 8))))
def increment(password):
    pass

