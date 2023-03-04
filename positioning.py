#!/usr/bin/python3

import itertools

permutations = list(itertools.permutations([1,1,1,0,0,0,0]))
print(len(permutations))

unique = set(permutations)
print((unique))
print(len(unique))

paths = 0
corrupted = 0
# Quorum at root and left
for entry in unique:
    # Left way
    paths = paths + 1
    is_corrupted = sum(entry[0:3]) == 3 or sum(entry[3:6]) == 3
    if is_corrupted: corrupted = corrupted + 1

    # Right way
    paths = paths + 1
    is_corrupted = sum(entry[0:3]) == 3 or entry[6] == 1
    if is_corrupted: corrupted = corrupted + 1

print('Number of corrupted when quorum is at root and left')
print(f'{paths} - {corrupted}: {corrupted/paths}')

paths = 0
corrupted = 0
# Quorum at left and right
for entry in unique:
    # Left way
    paths = paths + 1
    is_corrupted = entry[0] == 1 or sum(entry[1:4]) == 3
    if is_corrupted: corrupted = corrupted + 1

    # Right way
    paths = paths + 1
    is_corrupted = entry[0] == 1 or sum(entry[4:7]) == 3
    if is_corrupted: corrupted = corrupted + 1

print('Number of corrupted when quorum is at left and right')
print(f'{paths} - {corrupted}: {corrupted/paths}')


