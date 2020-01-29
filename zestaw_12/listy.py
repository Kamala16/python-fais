import random
import math
import matplotlib
import matplotlib.pyplot as plt

def int_0_N1(numberMax):
    # naturalNumberList = []
    # for item in range (numberMax-1):
    #     naturalNumberList.append(item)
    naturalNumberList = list(range(numberMax-1))
    random.shuffle(naturalNumberList)
    # plt.plot(range(numberMax-1), naturalNumberList, 'o')
    # plt.show()
    return naturalNumberList

def int_half_sort(numberMax):
    naturalNumberList = []
    for item in range(numberMax-1):
        if item % 4 == 0:
            naturalNumberList.append(random.randrange(numberMax))
        else:
            naturalNumberList.append(item)
    # plt.plot(range(numberMax-1), naturalNumberList, 'o')
    # plt.show()    
    return naturalNumberList

def int_half_sort_rev(numberMax):
    naturalNumberList = []
    for item in range(numberMax-1, 0, -1):
        if item % 4 == 0:
            naturalNumberList.append(random.randrange(numberMax))
        else:
            naturalNumberList.append(item)
    # plt.plot(range(numberMax-1), naturalNumberList, 'o')
    # plt.show()    
    return naturalNumberList

def float_gaus(numberMax):
    floatNumberList = []
    for item in range(numberMax):
        floatNumberList.append(random.gauss(0, 1))
    # plt.plot(range(numberMax), floatNumberList, 'o')
    # plt.show()
    return floatNumberList

def int_k(numberMax):
    intNumberList = []
    zbiorKMax = int(math.sqrt(numberMax))
    for item in range (numberMax):
        intNumberList.append(random.randrange(0, zbiorKMax))
    # plt.plot(range(numberMax), intNumberList, 'o')
    # plt.show()
    return intNumberList    
