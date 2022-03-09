# La manera en la que lo vamos a plantear es la siguiente: primero se coloca un numero, que actuara como pivote.
# Posteriormente colocamos el siguiente número que cumpla todas las condiciones. Después, otro más, y así sucesivamente.

from random import randint


n = 20
c = 10

t = [i + 1 for i in range(n)]

conditions = [(randint(1, n), randint(1, n)) for _ in range(c)]
conditions.sort()
print(conditions)


print("Ordenando {} elementos con {} condiciones".format(n, c))

def indexes(condition: tuple):
    i, j = condition
    a = t.index(i)
    b = t.index(j)
    return a, b

def check(condition: tuple) -> bool:
    a, b = indexes(condition)
    if a <= b:
        return True
    else:
        return False

def check_all(conditions: list):
    for condition in conditions:
        if not check(condition):
            return False
    return True







all_conditions_met = check_all(conditions)
i = 0
while not all_conditions_met:
    for condition in conditions:
        if not check(condition):
            first, second = indexes(condition)
            second_value = t.pop(second)
            t.insert(first + 1, second_value)

    all_conditions_met = check_all(conditions)

    #! Breaker
    i += 1
    if i >= 5000:
        print("Combination impossible to solve.")
        print("Close attempt:")
        break

print(t)
