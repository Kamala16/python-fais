def flatten(sequence):

    flat = []
    for i in sequence:
        if(isinstance(i, (list, tuple))):
            flat += flatten(i)
        else:
            flat.append(i)
    return flat

seq = [1, (2,3), [], [4,(5,6,7)], 8, 9]
print (flatten(seq))
