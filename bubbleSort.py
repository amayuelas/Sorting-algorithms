def bubbleSort(elements):
    """
    This funcion implements the BubbleSort algorithm
    BubbleSort is a stable algorithm (it does not change
    the order of two elements with same value) with a complexity O(n^2)
    @param  elements    List of elements to sort
    @return Sorted list of lements
    """
    i = 0
    swapped = True
    while (i < (len(elements)-1)) and (swapped==True):
        swapped = False
        for j in range(len(elements)-1):
            if elements[j]['rating'] < elements[j+1]['rating']:
                elements[j], elements[j+1] = elements[j+1],elements[j]
                swapped = True
        i+=1
    return elements
