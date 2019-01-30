def mergeSort(array):
    l = len(array)
    
    if l < 2:
        return array

    array1 = mergeSort(array[0:l//2])
    array2 = mergeSort(array[l//2:l])

    i1, i2, l1 = 0, 0, len(array1)
    
    while i1 + i2 < l:
        if i1 < l1 and (i2 == l1 or array1[i1] < array2[i2]):
            array[i1 + i2] = array1[i1]
            i1 = i1 + 1
        else:
            array[i1 + i2] = array2[i2]
            i2 = i2 + 1
        
    return array

print(mergeSort([7,33,55,-2,17,552,1,-26]))
