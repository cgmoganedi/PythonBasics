# Your input is a text and we decrypt it

alph2num = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9,
            'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17,
            'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}

num2alph = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J',
            10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R',
            18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z'}

stringRow1 = "DTKDX KYAGX KWAWL DTKYX QWYID OMKYC DODSR KDTKF"
stringRow2 = "YADMO XHYFD TOGQT WYITY JWLQL ORXOB FKIMX"
stringRow3 = "WDWLQ DTWAF OLQAK LDKLE KADXY LQKFS KLOGQ T"

ciphertext = stringRow1 + stringRow2 + stringRow3
ciphertext2 = "UETIL KNSWT VCPYD IYOCP"

def equation(C):
    return 17 * (C - 5)

def doCalculation(C):
    line = equation(C)
    while line > 25:
        line -= 26
    while line < 0 :
        line += 26
    return line

def decipher(string):
    ans = ""
    for char in string:
        C = alph2num[char]
        num = doCalculation(C)
        P = num2alph[num]
        ans += P
    return ans

def main():
    text = ciphertext2.replace(" ","")
    planeText = decipher(text)
    print(planeText)
