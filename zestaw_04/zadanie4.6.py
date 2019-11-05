def sum_seq(sequence):

    suma = 0
    for i in sequence:
        if(isinstance(i, (list, tuple))):
            suma += sum_seq(i)
            #print (suma)
        else:
            suma+= i
    return suma

S = [5, [], [4], (1,2), (5,6,7)]
print(sum_seq(S))
