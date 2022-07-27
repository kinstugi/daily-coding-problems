def euclidean(a,b):
    if b == 0: return 0
    a_prime = a % b
    return euclidean(b, a_prime)