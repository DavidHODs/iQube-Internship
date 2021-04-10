import random

def mergeSortAlg(array):
    print('\nSplitting array', array)
    if len(array) > 1:
        midPoint = len(array) // 2
        leftHalf = array[:midPoint]
        rightHalf = array[midPoint:]

        mergeSortAlg(leftHalf)
        mergeSortAlg(rightHalf)
        i = j = k = 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                array[k] = leftHalf[i]
                i=i+1
            else:
                array[k] = rightHalf[j]
                j=j+1
            k=k+1

        while i < len(leftHalf):
            array[k] = leftHalf[i]
            i=i+1
            k=k+1

    print('\nMerging array', array)


array = [random.randrange(1, 5000, 1) for i in range(5000)]

mergeSortAlg(array)

