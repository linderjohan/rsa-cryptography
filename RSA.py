import math
import sys

from Crypto.Util.number import inverse, getPrime


def alphabet():


def keygen(p: int, q: int) -> tuple:
    n = p * q
    # e = getPrime(p.bit_length())
    e = 9007
    d = inverse(e, (p-1)*(q-1))
    return e, d, n


def setPQ() -> int:
    if '-pq' in sys.argv:
        index1 = sys.argv.index('-pq') + 1
        index2 = sys.argv.index('-pq') + 2

        p = int(sys.argv[index1])
        q = int(sys.argv[index2])
    else:
        p = getPrime(30)
        q = getPrime(30)

    return p, q


def crypto(message: int, e: int, n: int) -> int:
    encrypted = pow(message, e, n)
    # decrypted = pow(encrypted, d, n)
    return encrypted


# n = p * q
def setMessage() -> int:
    if '-m' in sys.argv:
        index = sys.argv.index('-m') + 1
        message = str(sys.argv[index])
    else:
        message = 'cat'

    message = convertToInt(message)
    return message


def convertToInt(message: str) -> int:
    s = ''.join(str(ord(c)) for c in message)
    return int(s)


def convertToString()


str()
return


def printOut(n: int, e: int, d: int, message: int, encrypted: int, decrypted: int):
    print("PQ is: " + str(n))
    print("public key e is: " + str(e))
    print("private key d is: " + str(d))
    print("Message : " + str(message))
    print("Message Encrypted: " + str(encrypted))
    print("Decrypted : " + str(decrypted))
    return


p, q = setPQ()
message = setMessage()
e, d, n = keygen(p, q)
encrypted = crypto(message, e, n)
decrypted = crypto(encrypted, d, n)
printOut(n, e, d, message, encrypted, decrypted)


# # Python3 program for the above approach

# # Function to convert string to
# # integer without using functions
# def convert(s):

#     # Initialize a variable
#     num = 0
#     n = len(s)

#     # Iterate till length of the string
#     for i in s:

#         # Subtract 48 from the current digit
#         num = num * 10 + (ord(i) - 48)

#     # Print the answer
#     print(num)


# # Driver code
# if __name__ == '__main__':

#     # Given string of number
#     s = "123"

#     # Function Call
#     convert(s)

# # This code is contributed by Shivam Singh
