def partitionner(l, debut, fin):
    valeur_pivot = l[fin]
    indice_pivot = debut

    for i in range(debut, fin):
        if l[i] <= valeur_pivot:
            l[i], l[indice_pivot] = l[indice_pivot], l[i]
            indice_pivot += 1

    l[indice_pivot], l[fin] = l[fin], l[indice_pivot]
    return indice_pivot

def tri_rapide(l, debut=0, fin=None):
    if fin == None:
        fin = len(l)-1

    if fin > debut:

        pivot = partitionner(l, debut, fin)
        tri_rapide(l, debut, pivot-1)
        tri_rapide(l, pivot+1, fin)

l = [100, 63, 89, 54, 487, 78745, 14, 905, 1, 789, 468, 1245, 102, 77, 9214]
print(l)
tri_rapide(l)
print(l)