# Como T es un COMPARABLE, usaremos enteros, ya que estos son derivados de CCOMPARABLE, pero se puede usar
# cualquier tipo para el que la operación < o > esté definida

from random import randint

t = [randint(1, 100) for _ in range(20)]
print(t)

def change_position(obj_list: list, a: int, b: int):
    # x: variable temporal que almacena t[a] para cambiarlos
    x = obj_list[a]
    obj_list[a] = obj_list[b]
    obj_list[b] = x

simple_sort_t = t.copy()
def simple_sort(list_to_sort: list):
    for i in range(len(list_to_sort)):
        while True:
            if i <= 0:
                break
            elif t[i] >= t[i-1]:
                break
            else:
                change_position(simple_sort_t, i, i-1)
                i -= 1

simple_sort(simple_sort_t)
print(simple_sort_t)

dicotomy_sort_t = t.copy()
def dicotomy_sort(list_to_sort: list):
    final = []
    for i in list_to_sort:
        pass

#! Not finished