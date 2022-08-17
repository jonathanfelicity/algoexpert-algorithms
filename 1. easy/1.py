def rotate(n, d):
    tem = n[:d]
    new_array = n[d:]
    for i in tem:
        new_array.append(i)
    return new_array
    
    

