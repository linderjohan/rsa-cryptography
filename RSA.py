# import math
import sys

from Crypto.Util.number import inverse, getPrime


def keygen(x: int, y: int) -> tuple:
    xy = x * y
    ex = getPrime(x.bit_length())
    # ex = 9007
    dy = inverse(ex, (x-1)*(y-1))
    return ex, dy, xy


def setPQ() -> int:
    if '-pq' in sys.argv:
        index1 = sys.argv.index('-pq') + 1
        index2 = sys.argv.index('-pq') + 2

        pe = int(sys.argv[index1])
        qu = int(sys.argv[index2])
    else:
        pe = getPrime(30)
        qu = getPrime(30)

    return pe, qu


def crypto(mes: int, exponent: int, mods: int) -> int:
    enc = pow(mes, exponent, mods)
    # decrypted = pow(encrypted, d, n)
    return int(enc)


def setMessage() -> int:
    if '-m' in sys.argv:
        index = sys.argv.index('-m') + 1
        m = str(sys.argv[index])
        print(m)
    else:
        m = 'cat'

    # message = convertToInt(message)
    return m


def convertToInt(messageS: str) -> int:
    # s = ''.join(str(ord(c)) for c in message)
    st = ''
    for c in messageS:
        st += str(ord(c) * 1000)

    print(int(st))
    return int(st)

# cat 99000 97000 116000
#  9900097000119000


def convertToString(s: int):
    print("INT: " + str(s))

    text = ''
    divider = 1000

    while s > 0:
        s = int(s/1000)
        mod = int(s % 1000) < 100
        text = chr(int(s % 1000)) + text

        divider = 100 if mod else 1000
        s = int(s/divider)

    return text


def printOut(es, des, messageG, encryptedT, decryptedT):
    print("public key e is: " + str(es))
    print("private key d is: " + str(des))
    print("Message : " + str(messageG))
    print("Message Encrypted: " + str(encryptedT))
    print("Decrypted : " + str(decryptedT))
    return


def main():
    p, q = setPQ()
    message = setMessage()
    message = convertToInt(message)
    print("message is: " + str(message))
    e, d, n = keygen(p, q)
    encrypted = crypto(message, e, n)
    print("encrypted 1st: " + str(encrypted))
    decrypted = crypto(encrypted, d, n)
    print("decrypted 1st: " + str(decrypted))
    decrypted = convertToString(decrypted)
    printOut(e, d, message, encrypted, decrypted)


if __name__ == "__main__":
    main()


# print(oct(101))
#     # Print the answer


#     # Given string of number
#     s = "123"
