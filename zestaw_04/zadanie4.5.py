def odwracanie_iter(L, left, right):
    
    i = 0
    temp = 0
    while i < (len(L)/2):
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        
        left+=1
        right-=1
        i+=1
    return L

def odwracanie_rek(L, left, right):

    if(left < len(L)/2):
        L = odwracanie_rek(L, left+1, right-1)
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
    return L

L = [1, 2, 3, 4, 5]
print ("sposób iteracyjny:")
print (odwracanie_iter(L, 0, len(L)-1))
L = [1, 2, 3, 4, 5]
print ("sposób rekurencyjny:")
print (odwracanie_rek(L, 0, len(L)-1))
