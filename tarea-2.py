from random import randint

t = list(range(1, 11))

conditions = [(randint(1, 10), randint(1, 10)) for _ in range(5)]
conditions.sort()
print(conditions)

t = [i+1 for i in range(10)]

def check(condition: tuple) -> bool:
    i, j = condition
    a = t.index(i)
    b = t.index(j)
    if a <= b:
        return True
    else:
        return False

print(check(conditions[1]))