"""
Pseudocódigo:
INICIO

- para cada elemento i no array de tamanho n
    - para cada elemento j no array de tamanho n - 1
        - se elemento i for maior que elemento j
            - troque os elementos i e j
- Exiba o array ordenado 

FIM
"""

lista = [6, 7, 8, 3, 10, 19, 4, 1, 0, 61, 30, 16, 17, 82, 29, 34, 43, 21, 11, 39, 56, 67, 12]

def bubble_sort(arr):

    n = len(arr)

    #para cada elemento i do array
    for i in range(n):
        #para cada elemento j do array
        for j in range(0, n-i-1):
            #se elemento i for maior que elemento j
            if arr[j] > arr[j+1]:
                #troque os elementos i e j
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    