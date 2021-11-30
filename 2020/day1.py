import numpy as np
databestand = open('data/input_for_day1.txt', 'r')
legelijst = []
for i in range(200):
    regel = databestand.readline()
    legelijst.append(int(regel))
for i in range(200):
    res = 2020 - legelijst[i]
    for j in range(200):
        resres = res - legelijst[j]
        if resres in legelijst:
            print(resres* legelijst[i]*legelijst[j])