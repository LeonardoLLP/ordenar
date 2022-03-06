from random import randint

t = [randint(1, 1000) for _ in range(100)]
print(t)

t_split = []

t_max = 0
j = 0
for i in range(len(t)):
    if t[i] >= t_max:
        t_max = t[i]
        t_split.append(t[j:i+1])
        j = i+1

print(t_split)
