def minimumSwaps(arr):
    elem_idx_dict = {elem: idx for idx, elem in enumerate(arr)}
    swap = 0
    for i, elem in enumerate(arr):  # O(n)
        if elem != i + 1:
            correct_elem_idx = elem_idx_dict[i+1]  # O(1)
            arr[i], arr[correct_elem_idx] = arr[correct_elem_idx], arr[i]
            elem_idx_dict[elem] = correct_elem_idx
            elem_idx_dict[i+1] = i
            swap += 1
    return swap 
         
    
     
    