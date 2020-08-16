# _ 1 2 3 4 5 6 7 8 9
# A _ _ _ _ _ _ x x _
# B _ x _ _ _ _ _ _ _
# C _ x _ _ _ _ _ _ _
# D _ x _ _ _ _ _ _ _
# E _ _ x x x _ _ x _
# F _ _ _ _ _ _ _ x _
# G _ _ _ _ _ _ _ x _
# H _ x x _ _ _ _ x _
# I _ _ _ x x _ _ _ _
# A1
# B2
# C3
# D4
# E5
# F9
# G8
# I4
# H3
# H2

n = 9
_ = input().split()
field = {}
for i in range(n):
    s = input().split()
    field[s[0]] = s[1:]

letters = list()
nums = list()
for _ in range(10):
    target = input()
    letters.append(target[0])
    nums.append(int(target[1]))

for i in range(10):
    arr = field[letters[i]]
    if arr[nums[i] - 1] == 'x':
        print("Попал!")
    else:
        print("Промах!")
