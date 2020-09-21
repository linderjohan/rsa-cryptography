import math
import sys

# print('hello world')


def is_prime(n):
    if n == 2:
        return True

    if n % 2 == 0 or n <= 1:
        return False

    for i in range(2, int(n/2)):
        if n % i == 0:
            return False

    return True


if '-pq' in sys.argv:
    index1 = sys.argv.index('-pq') + 1
    index2 = sys.argv.index('-pq') + 2

    p = int(sys.argv[index1])
    q = int(sys.argv[index2])

    if not is_prime(p) or not is_prime(q):
        raise ValueError('P or Q were not prime')

else:
    p = 1669
    q = 1993
    # keygen.py -pq 233 454
    # [keygen.py, -pq, 233, 454]

n = p * q

# if(math.gcd(e, (p-1)*(q-1)) == 1):
# for i in range((p-1)*(q-1), 1, -1):
#     if is_prime(i):

#         e = int(i)
#         break
# else:
#     e = 1993


phi = (p-1)*(q-1) + 1
e = 9000
d = 1

de = d * e

while de != phi:
    e += 1
    d = int(phi / e)
    de = d * e
# d = de / e
# d = modinverse(e, (p-1)*(q-1))

# d = 1s
# de = d * e
# while de != phi

# d*e = 1 (mod phi)
# print("private key d is: " + str(d))
# Encrypt: (message^x) % PQ
# Decrypt: (message^y) % PQ

print("PQ is: " + str(n))
print("public key e is: " + str(e))
print("private key d is: " + str(d))
