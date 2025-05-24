import itertools

lst = [1, 2, 3]
hoan_vi = list(itertools.permutations(lst))

print("Tất cả các hoán vị của danh sách [1, 2, 3]:")
for perm in hoan_vi:
    print(perm)
