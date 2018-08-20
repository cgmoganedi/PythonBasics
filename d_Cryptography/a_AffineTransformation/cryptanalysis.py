from collections import Counter

stringRow1 = "DTKDX KYAGX KWAWL DTKYX QWYID OMKYC DODSR KDTKF"
stringRow2 = "YADMO XHYFD TOGQT WYITY JWLQL ORXOB FKIMX"
stringRow3 = "WDWLQ DTWAF OLQAK LDKLE KADXY LQKFS KLOGQ T"

ciphertext = stringRow1 + stringRow2 + stringRow3

ciphertext2 = "UETIL KNSWT VCPYD IYOCP"

def getMostCommon(string):
    # returns the two most common charaters
    string = string.replace(" ","")
    c = Counter(string)
    return c.most_common(2)

def main():
    #string = input("Enter type in the string of interest below.\n")
    string = ciphertext2
    common = getMostCommon(string)
    print("The most common character is: ", common[0][0])
    print("It occurs ", common[0][1]," times.")
    print("The second most common character is: ", common[1][0])
    print("It occurs ", common[1][1]," times.")
    # Assume common[0] -> E
    # Assume common[1] -> T

'''
def solveEquations():
    return
    
import sys
sys.setrecursionlimit(1000000)  # long type,32bit OS 4B,64bit OS 8B(1bit for sign)

# return (g, x, y) a*x + b*y = gcd(x, y)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

# x = mulinv(b) mod n, (x * b) % n == 1
def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n
'''
