# Como T es un COMPARABLE, usaremos enteros, ya que estos son derivados de CCOMPARABLE, pero se puede usar
# cualquier tipo para el que la operación < o > esté definida

from pyclbr import Function
from random import randint
from time import time

n = 10000

print("Ordenando {} elementos \n".format(n))
t = [randint(1, 100) for _ in range(n)]
# print(t)
# print()

def change_position(obj_list: list, a: int, b: int):
    # x: variable temporal que almacena t[a] para cambiarlos
    x = obj_list[a]
    obj_list[a] = obj_list[b]
    obj_list[b] = x

def execute_algorythm(sort: Function, list_to_order: list, print_list: bool = False):
    initial_time = time()
    sort(list_to_order)
    total = time() - initial_time
    if print_list:
        print(list_to_order)
    print("Algorythm: {}".format(sort))
    print("Execution time: {}".format(total))
    print()



simple_sort_t = t.copy()
def simple_sort(list_to_sort: list):
    for i in range(len(list_to_sort)):
        while True:
            if i <= 0:
                break
            elif simple_sort_t[i] >= simple_sort_t[i-1]:
                break
            else:
                change_position(simple_sort_t, i, i-1)
                i -= 1

execute_algorythm(simple_sort, simple_sort_t)



dicotomy_sort_t = t.copy()
def dicotomy_sort(list_to_sort: list):
    final = []
    for element in list_to_sort:
        min_x = 0
        max_x = len(final) - 1

        while True:
            if min_x > max_x:
                final.insert(min_x, element)  # IMPORTANT: min_x is necessary, it inserts it where the less amount is needed
                break
            else:
                i = (min_x + max_x) // 2
                if element > final[i]:
                    min_x = i + 1
                else:  # element <= final[i]
                    max_x = i - 1

    list_to_sort = final.copy()

execute_algorythm(dicotomy_sort, dicotomy_sort_t)



god_mode_sort_t = t.copy()
def god_mode_sort(list_to_sort: list):
    list_to_sort.sort()

execute_algorythm(god_mode_sort, god_mode_sort_t)
