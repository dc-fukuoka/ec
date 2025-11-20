#!/usr/bin/env python3

# elliptic curver over finite field F_7
# y^2 = x^3 + ax + b mod p
# a = 1, b = 1, p = 7

p = 7
a = 1
b = 1

G = (0, 1)  # base point
n = 5       # order #E(F_p) = 5

# group add for E(F_p)
def point_add(P, Q):
    # P + O = P, O + Q = Q
    if P == "O":
        return Q
    if Q == "O":
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return "O"  # P + Q = O

    if P == Q:
        # same point, P + P
        num = (3*x1**2 + a) % p
        den = (2*y1) % p
    else:
        # different point, P + Q
        num = (y2 - y1) % p
        den = (x2 - x1) % p

    # calculate inverse
    # note: pow(n, -1, p) calculates the inverse over mod(p)
    den_inv = pow(den, -1, p)

    lam = (num * den_inv) % p

    x3 = (lam**2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return (x3, y3)

# calculate n * G
multiples = []
current = G
for i in range(1, n+2):
    multiples.append(current)
    current = point_add(current, G)

# output
print(f"Elliptic curve: y^2 = x^3 + x + 1 over F_{p}")
print(f"Base point G = {G}")
for i, P in enumerate(multiples, 1):
    print(f"{i}*G = {P}")

# Q = d * G
# Q: public key
# d: private key
