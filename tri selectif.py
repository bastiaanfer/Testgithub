def insertion(l):
    for indice in range(len(l)):
        j = indice
        while j > 0 and l[j-1] > l[j]:
            l[j], l[j-1] = l[j-1], l[j]
            j-=1


l = [11, 39, 9, 2, 8, 87, 92, 63, 74, 9, 5, 69, 63, 33, 46]
print(l)
insertion(l)
print(l)