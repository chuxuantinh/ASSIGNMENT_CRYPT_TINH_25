from string import ascii_uppercase
from random import randint
import sys

# Pi
def dic_anpha():
    ret = {}
    c = 0
    for i in ascii_uppercase:
        ret[i] = c
        c += 1
    for i in range(0, 26):
        ret[i] = ascii_uppercase[i]
    return ret
    #print(ret)


def usage():
    sys.stdout.write("usage: python enc_aff.py [plaintext file] (a) (b)")
    sys.stdout.write("\n\ta gcd(a,m)= 1\n")
    sys.exit(0)

def checkInput():
    if len(sys.argv) == 1:
        sys.stdout.write("Not found file plaintext.\n\n")
        usage()

    elif len(sys.argv) == 4:
        sys.stdout.write("Key (" + sys.argv[2] + ", " + sys.argv[3] +")\n")

    elif len(sys.argv) > 2:
        sys.stdout.write("Parameter input?!\n\n")
        usage()

def openFile():
    try:
        file_input = open(sys.argv[1])
    except IOError:
        print("parameter" + sys.argv[1] + " does not exist.")
        sys.exit(0)
    return file_input

checkInput()
file_input = openFile()

plaintext = ""

for i in file_input:
    plaintext += i

plaintext = plaintext.upper()


file_input.close()

#Get uppercase aplhabet mapped to numbers 0 - 25
alph = dic_anpha()

#cc = (ax + b) % 26 where x is a plaintext


def factor(x):
    ret = []
    for i in range(1, x):
        if ((x // i) - (x / i)) == 0:
            ret.append(i)
    return ret

# tim a hop le gcd(a,m) = gcd(a,26) =1
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

#Random => a, b
def randomA(modulus):
    t = 0
    while t not in findA(modulus):
        t = randint(2, modulus)
    return t

def randomB(modulus):
    return randint(0, modulus)


m = 26


if len(sys.argv) == 4:
    try:
        a = int(sys.argv[2])
    except ValueError:
        sys.stdout.write("Parameter missing!\n")
        sys.stdout.write("Input: " + sys.argv[2] + "\n\n")
        usage()
    try:
        b = int(sys.argv[3])
    except ValueError:
        sys.stdout.write("Parameter missing!\n")
        sys.stdout.write("Input: " + sys.argv[3] + "\n\n")
        usage()

    temp = b
    b = b % 26
    if temp != b:
        sys.stdout.write("Your input "+ str(temp) + " was mod by 26 and has become " + str(b) + ".\n")
    if a not in findA(m):
        sys.stdout.write("value is not in legal set of values:\n")
        sys.stdout.write(str(findA(m)) + "\n\n")
        usage()

else:
    a = randomA(m)
    b = randomB(m)

def enc_aff(plainText, a, b, modulus):
    ret =[]
    for x in plainText:
        if x in alph:
            x = alph[x]
            e = ((a * x) + b) % 26
            sys.stdout.write(str(alph[e]))
            #print(x)
        else:
            #None
            sys.stdout.write(x)


    sys.stdout.write("\n\n")
    return ret

reenc =[]
reenc.append((enc_aff(plaintext,a,b,m)))
print("Your plaintext , "+plaintext+"")
enc_aff(plaintext, a, b, m)
#print("Table:("+str(dic_anpha())+")")
#print("Plaintext " +ptext+" Your text was encrypted with key (" + str(a) + ", " + str(b) + ","'ssss'", " + str(findA(m)) + ")")
print("was encrypted with key (" + str(a) + ", " + str(b) + ","'  With a is number random in list '"," + str(findA(m)) + ")")
