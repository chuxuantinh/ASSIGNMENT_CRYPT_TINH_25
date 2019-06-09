from string import ascii_uppercase
import sys


def dic_anpha():
    ret = {}
    c = 0
    for i in ascii_uppercase:
        ret[i] = c
        c += 1
    for i in range(0, 26):
        ret[i] = ascii_uppercase[i]
    return ret


def usage():
    sys.stdout.write("usage: python dec_aff.py [ciphertext file]")
    sys.exit(0)


def checkInput():
    if len(sys.argv) == 1:
        sys.stdout.write("Not found ciphertext file.\n\n")
        usage()

    if len(sys.argv) > 2:
        sys.stdout.write("too much input!\n\n")
        usage()

def openFile():
    try:
        file_input = open(sys.argv[1])
    except IOError:
        print("File " + sys.argv[1] + " does not exist.")
        sys.exit(0)
    return file_input

checkInput()
file_input = openFile()

cipher_text = ""


for i in file_input:
    cipher_text += i

cipher_text = cipher_text.upper()

file_input.close()


alph = dic_anpha()

def compMMInverse(a, m):
    for i in range(1, m):
        if ((a * i) % m) == 1:
            return i


def factor(x):
    ret = []
    for i in range(1, x):
        if ((x // i) - (x / i)) == 0:
            ret.append(i)
    return ret


def findA(m):
    factors = factor(m)
    ret = []
    for i in range(2, m):
        append = True
        for j in factors[1:]:
            if i % j == 0:
                append = False
        if append:
            ret.append(i)
    return ret


m = 26
a = findA(m)


def Dec_aff(ciphText, aValues, modulus):
    c = 1
    for a in aValues:
        mmi = compMMInverse(a, modulus)
        for b in range(0, modulus):
            sys.stdout.write("Attempt #" + str(c) + "\n")
            sys.stdout.write("Key Pair: (" + str(a) + ", " + str(b) + ")\n")
            for x in ciphText:

                #Dec_aff(x) = a^-1 (x - b) mod m

                if x in alph:
                    x = alph[x]
                    d = mmi * (x - b) % m
                    sys.stdout.write(str(alph[d]))
                else:
                    try:
                        sys.stdout.write(x)
                    except UnicodeEncodeError:
                        sys.stdout.write("")
            sys.stdout.write("\n\n")
            c += 1

Dec_aff(cipher_text, a, m)
