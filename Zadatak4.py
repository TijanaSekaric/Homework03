#maksimum liste

def Max(list):

    if len(list) == 1:
        return list[0]

    else:
        return max(list[0],max(list[1:]))


lista=[18,88,188]
print(max(lista))

