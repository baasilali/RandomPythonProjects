#Baasil Ali
# 11 / 17 / 2022

#This program contains four functions which calculate the reciprocal of a number. 

import math

def reciprocal(a):
    if a != 0:
        return round(1/a, 1)
    else:
        print('ERROR - Divide by zero')

def mean(a, b, c):
    return round((a + b + c) / 3, 1)

def geometric_mean(a, b, c):
    product = a * b * c

    gm = (float)(math.pow(product, (1 / 3)))
    return round((float)(gm), 1)

def harmonic_mean(a, b, c):

    if a!= 0 and b != 0 and c!= 0:
        sum = reciprocal(a) + reciprocal(b) + reciprocal(c)
        hm = (float)(3 / sum)
        return round(hm, 1)
    else:
        return('ERROR - Divide by zero')

a = 10
b = 11
c = 12

print('Reciprocal of', a, 'is: ', reciprocal(a))
print('Reciprocal of', b, 'is: ', reciprocal(b))
print('Reciprocal of', c, 'is: ', reciprocal(c))

print('Arithmetic mean is: ', mean(a, b, c))
print('Geometric mean is: ', geometric_mean(a, b, c))
print('Harmonic mean is: ', harmonic_mean(a, b, c))




