# import math
import sys

from Crypto.Util.number import inverse, getPrime


def keygen(p: int, q: int):
    # Calculate n
    n = p * q
    # Get a large prime for exponent
    e = getPrime(1024)
    # e = 9007
    # Calculate the modular inverse for e with p and q
    d = inverse(e, (p-1)*(q-1))
    return e, d, n


def setPQ():
    p = getPrime(512)
    q = getPrime(512)
    return p, q


def crypto(message: int, exponent: int, mod: int):
    # Encrypt/Decrypt with modular exponent
    crypted = pow(message, exponent, mod)

    return int(crypted)


def setMessage():
    # Read message from arguments sent to the program
    if '-m' in sys.argv:
        index = sys.argv.index('-m') + 1
        message = str(sys.argv[index])
    else:
        message = "Cat"
    # convert the plain text to integer form
    message = convertToInt(message)
    return message


def convertToInt(message: str):
    text = ''
    for c in message:
        text += str(ord(c) * 1000)

    return int(text)


def convertToString(s: int):

    text = ''
    divider = 1000

    while s > 0:
        s //= 1000
        mod = int(s % 1000) < 100
        text = chr(int(s % 1000)) + text
        divider = 100 if mod else 1000
        s //= divider

    return text


def printOut(e, d, message, encrypted, decrypted):
    print("Public key e is: " + str(e))
    print("")
    print("Private key d is: " + str(d))
    print("")
    print("Message: " + str(message))
    print("")
    print("Message Encrypted: " + str(encrypted))
    print("")
    print("Decrypted message: " + str(decrypted))
    return


def main():
    p, q = setPQ()  # set primes for p and q (512bits)
    message = setMessage()  # read message from commandline
    # generate public key e, calculate private key d and n = p * q
    e, d, n = keygen(p, q)
    encrypted = crypto(message, e, n)  # encrypt the incoming message
    decrypted = crypto(encrypted, d, n)  # decrypt the encrypted message
    # convert the encrypted message back to a string
    decrypted = convertToString(decrypted)
    printOut(e, d, message, encrypted, decrypted)


if __name__ == "__main__":
    main()
