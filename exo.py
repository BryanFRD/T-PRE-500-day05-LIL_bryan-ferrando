l = [1, 2, 3, 4, 5]
print(f"{l[0]} - {l[-1]}")

l.append(6)
print(*l)

l.pop()
print(*l)

l.insert(0, -1)
print(*l)

print(*l[2:6])

reversed = l[::-1]
print(*reversed)

print(f"{l[0]} - {reversed[0]}")

for c in range(-10, -27, -1):
  reversed.append(c)
print(*reversed)

l = [2, 44, 5, 6, 47, 6, 7, 94, 123, 67]
m = 1
for i in l:
  m *= i
print(m)

print([x+10 for x in [3, 2, 6, 7, 1, 4]])

l = list(map(lambda x: x*x, [3, 2, 6, 7, 1, 4]))
print(l)

print(f"{min(l)} - {max(l)}")

print(*filter(lambda x: x < 7, l))

l.sort()
print(l)

t = [x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]]
print(t)

print(*filter(lambda x: x > 10, [42, 3, 4, 18, 3, 10]))

print([*enumerate([42, 3, 4, 18, 3, 10])])

first_name = ["Jackie", "Bruce", "Arnold", "Sylverster"]
last_name = ["Stallone", "Schwarzenegger", "Willis", "Chan"]

magic = [*zip(first_name, last_name[::-1])]

print(magic[0])
print(magic[3])
print(magic[1][0])
print(magic[0][1])
print(magic[2])

import time, random

starting_time = time.time()
l = []
for i in range(0, 1_000_000):
  l.append(random.random())

print(time.time() - starting_time)

