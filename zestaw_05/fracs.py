from math import gcd    #fractions.gcd() is deprecated

def add_frac(frac1, frac2):
    
    nww = frac1[1]*frac2[1]/gcd(frac1[1], frac2[1])
    frac1[0] = frac1[0]*(nww/frac1[1])
    frac2[0] = frac2[0]*(nww/frac2[1])
    suma = [frac1[0] + frac2[0], nww]
    return suma
    
def sub_frac(frac1, frac2):

    nww = frac1[1]*frac2[1]/gcd(frac1[1], frac2[1])
    frac1[0] = frac1[0]*(nww/frac1[1])
    frac2[0] = frac2[0]*(nww/frac2[1])
    roznica = [frac1[0]-frac2[0], nww]
    return roznica

def mul_frac(frac1, frac2):

    mnozenie = [frac1[0]*frac2[0], frac1[1]*frac2[1]]
    return mnozenie

def div_frac(frac1, frac2):
    
    dzielenie = [frac1[0]*frac2[1], frac1[1]*frac2[0]]
    return dzielenie

def is_positive(frac):
    
    if((frac[0] > 0 and frac[1] > 0) or (frac[0] <= 0 and frac[1] < 0)):
        return True
    else:
        return False

def is_zero(frac):

    if(frac[0] == 0):
        return True
    else:
        return False

def cmp_frac(frac1, frac2):

    nww = frac1[1]*frac2[1]/gcd(frac1[1], frac2[1])
    frac1[0] = frac1[0]*(nww/frac1[1])
    frac2[0] = frac2[0]*(nww/frac2[1])
    if(frac1[0] > frac2[0]):
        return -1
    elif(frac1[0] == frac2[0]):
        return 0
    elif(frac1[0] < frac2[0]):
        return 1

def frac2float(frac):

    return float(frac[0]/frac[1])

f1 = [1, 2]
f2 = [1, 3]
print(cmp_frac(f1, f2))
