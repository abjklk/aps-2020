# The Chudnovsky algorithm is a fast method for calculating the digits of π, based on Ramanujan’s π formulae.

from decimal import Decimal as Dec, getcontext as gc

def PI(maxK: int = 70, prec: int = 1008, disp: int = 1007):  # Parameter defaults chosen to gain 1000+ digits within a few seconds
    gc().prec = prec
    K, M, L, X, S = 6, 1, 13591409, 1, 13591409
    for k in range(1, maxK + 1):
        M = (K**3 - 16*K) * M // k**3 
        L += 545140134
        X *= -262537412640768000
        S += Dec(M * L) / X
        K += 12
    pi = 426880 * Dec(10005).sqrt() / S
    pi = Dec(str(pi)[:disp])  # Drop few digits of precision for accuracy
    print("PI(maxK={} iterations, gc().prec={}, disp={} digits) =\n{}".format(maxK, prec, disp, pi))
    return pi

Pi = PI()
# print("\nFor greater precision and more digits (takes a few extra seconds) - Try")
# print(PI(317, 4501, 4500))
# print(PI(353, 5022, 5020))