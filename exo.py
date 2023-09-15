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

r_starting_time = time.time()
l = []
for i in range(0, 1_000_000):
  l.append(random.randint(0, 1_000_000))
r_time = time.time() - r_starting_time
print(f"Random generation time: {r_time*1000:.3f} ms")

l = [9, 1, 3, 2, 6, 7, 8, 4, 5]

s_starting_time = time.time()

def merge_sort(ls):
  if len(ls) <= 1:
    return ls
  lft = []
  rgt = []
  for i in range(len(ls)):
    t = ls[i]
    if i < (len(ls) / 2):
      lft.append(t)
    else:
      rgt.append(t)
      
  lft = merge_sort(lft)
  rgt = merge_sort(rgt)
    
  r = []
  while lft and rgt:
    if lft[0] <= rgt[0]:
      r.append(lft[0])
      lft.pop(0)
    else:
      r.append(rgt[0])
      rgt.pop(0)
  
  r.extend(lft)
  r.extend(rgt)
  
  return r
  
l = merge_sort(l)
s_time = time.time() - s_starting_time
print(f"Sorting time: {s_time*1000:.3f} ms")
print(f"Total time: {(r_time + s_time)*1000:.3f} ms")
print(*l)