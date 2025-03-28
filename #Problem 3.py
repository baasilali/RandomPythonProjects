#Problem 3

for a in range(1, 999):
    for b in range(a+1, 1000):
        for c in range(b+1, 1001):
            if a*a + b*b == c*c:
                print(a, b, c)




