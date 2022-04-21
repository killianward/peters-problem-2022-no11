# Peter's Problem 2022 No.11

from itertools import permutations

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_valid(perm):
    c = str(perm[0])
    a = str(perm[1])
    r = str(perm[2])
    e = str(perm[3])
    err = int(e + r + r)
    care = int(c + a + r + e)
    if err + err == care:
        return True
    else:
        return False

for perm in list(permutations(digits, 4)):
    if is_valid(perm):
        print(f"Answer: {perm}")
        break
