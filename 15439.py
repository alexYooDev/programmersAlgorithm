from itertools import permutations

N = int(input())

outfit_choice = list(permutations(range(N), 2))

print(len(outfit_choice))