from random import randint

# Modified variation just for purposes of visualisation
t = [randint(1, (i+1)*10) for i in range(100)]
print(t)
print()

#! Split
t_split = []
t_max = 0
j = 0
for i in range(len(t)):
    if t[i] >= t_max:
        t_max = t[i]
        t_split.append(t[j:i])
        j = i
t_split.pop(0)
print(t_split)
print()

#! Change order of list
for numbers in t_split:
    last = numbers.pop(0)
    numbers.append(last)

print(t_split)
print()


#! Put together tables
t_final = []
for numbers in t_split:
    t_final.extend(numbers)

print(t_final)
print()