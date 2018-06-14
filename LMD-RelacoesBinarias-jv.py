import math


# A = {1,2,3,4}  pares: (1,1) (1,2) (1,3) (1,4) (2,1) (2,2) (2,3) (2,4) (3,1) (3,2) (3,3) (3,4) (4,1) (4,2) (4,3) (4,4) mapeados em 16 bits
def classifica(r):

    b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    b[0] = r & 32768 == 32768 #(1,1)
    b[1] = r & 16384 == 16384 #(1,2)
    b[2] = r & 8192 == 8192 #(1,3)
    b[3] = r & 4096 == 4096 #(1,4)
    b[4] = r & 2048 == 2048 #(2,1)
    b[5] = r & 1024 == 1024 #(2,2)
    b[6] = r & 512 == 512 #(2,3)
    b[7] = r & 256 == 256 #(2,4)
    b[8] = r & 128 == 128 #(3,1)
    b[9] = r & 64 == 64 #(3,2)
    b[10] = r & 32 == 32 #(3,3)
    b[11] = r & 16 == 16 #(3,4)
    b[12] = r & 8 == 8 #(4,1)
    b[13] = r & 4 == 4 #(4,2)
    b[14] = r & 2 == 2 #(4,3)
    b[15] = r & 1 == 1 #(4,4)

    classe = ""
    x = r & 33825
    if x == 33825:
        classe += "R"
    if x != 33825:
        classe += "I"

    flagS=1
    if b[14]!=b[11]:
        flagS = 0
    if b[13]!=b[7]:
        flagS = 0
    if b[12]!=b[3]:
        flagS = 0
    if b[9]!=b[6]:
        flagS = 0
    if b[8]!=b[2]:
        flagS = 0
    if b[4]!=b[1]:
        flagS = 0
    if flagS == 1:
        classe += "S"


    flagT = 1
    if b[14] == 1 and b[9] == 1:
        if b[13] == 0:
            flagT = 0
    if b[14] == 1 and b[8] == 1:
        if b[12] == 0:
            flagT = 0
    if b[13] == 1 and b[6] == 1:
        if b[14] == 0:
            flagT = 0
    if b[13] == 1 and b[4] == 1:
        if b[12] == 0:
            flagT = 0
    if b[12] == 1 and b[2] == 1:
        if b[14] == 0:
            flagT = 0
    if b[12] == 1 and b[1] == 1:
        if b[13] == 0:
            flagT = 0
    if b[11] == 1 and b[12] == 1:
        if b[8] == 0:
            flagT = 0
    if b[11] == 1 and b[13] == 1:
        if b[9] == 0:
            flagT = 0
    if b[9] == 1 and b[7] == 1:
        if b[11] == 0:
            flagT = 0
    if b[9] == 1 and b[4] == 1:
        if b[8] == 0:
            flagT = 0
    if b[8] == 1 and b[1] == 1:
        if b[9] == 0:
            flagT = 0
    if b[8] == 1 and b[3] == 1:
        if b[11] == 0:
            flagT = 0
    if b[7] == 1 and b[12] == 1:
        if b[4] == 0:
            flagT = 0
    if b[7] == 1 and b[14] == 1:
        if b[6] == 0:
            flagT = 0
    if b[6] == 1 and b[8] == 1:
        if b[4] == 0:
            flagT = 0
    if b[6] == 1 and b[11] == 1:
        if b[7] == 0:
            flagT = 0
    if b[4] == 1 and b[2] == 1:
        if b[6] == 0:
            flagT = 0
    if b[4] == 1 and b[3] == 1:
        if b[7] == 0:
            flagT = 0
    if b[3] == 1 and b[13] == 1:
        if b[1] == 0:
            flagT = 0
    if b[3] == 1 and b[14] == 1:
        if b[2] == 0:
            flagT = 0
    if b[2] == 1 and b[9] == 1:
        if b[1] == 0:
            flagT = 0
    if b[2] == 1 and b[11] == 1:
        if b[3] == 0:
            flagT = 0
    if b[1] == 1 and b[6] == 1:
        if b[2] == 0:
            flagT = 0
    if b[1] == 1 and b[7] == 1:
        if b[3] == 0:
            flagT = 0
    if flagT == 1:
        classe += "T"


    if classe == "RST":
        classe += "E"
    flagF = 0
    if r > 4096:
        flagF = 1
        if r & 15 == 0:
            flagF = 0
            if r & 240 < 16 :
                flagF = 0
                if r & 3840 < 256:
                    flagF = 0
        if flagF==1:
            classe += "F"
        flagbsi=1
        x = r & 61440
        if not isinstance(math.log(x, 2), float):
            flagbsi = 0
        elif r << 4 == x / 16 or r << 8 == x / 256 or r << 12 == x / 4096:
            flagbsi = 0
        x = r & 3840
        if x == 0:
            flagbsi = 0
        if x != 0:
            if not isinstance(math.log(x, 2), float):
                flagbsi = 0
            elif r << 4 == x / 16 or r << 8 == x / 256:
                flagbsi = 0
        x = r & 240
        if x == 0:
            flagbsi = 0
        if x != 0:
            if not isinstance(math.log(x, 2), float):
                flagbsi = 0
            elif r << 3 == x / 16:
                flagbsi = 0
        x = r & 15
        if x == 0:
            flagbsi = 0
        if x != 0:
            if not isinstance(math.log(x, 2), float):
                flagbsi = 0
        if flagbsi==1:
            classe += "FbFsFi"


    resp = "{"
    if b[0]:
        resp += "(1,1)"
    if b[1]:
        resp += "(1,2)"
    if b[2]:
        resp += "(1,3)"
    if b[3]:
        resp += "(1,4)"
    if b[4]:
        resp += "(2,1)"
    if b[5]:
        resp += "(2,2)"
    if b[6]:
        resp += "(2,3)"
    if b[7]:
        resp += "(2,4)"
    if b[8]:
        resp += "(3,1)"
    if b[9]:
        resp += "(3,2)"
    if b[10]:
        resp += "(3,3)"
    if b[11]:
        resp += "(3,4)"
    if b[12]:
        resp += "(4,1)"
    if b[13]:
        resp += "(4,2)"
    if b[14]:
        resp += "(4,3)"
    if b[15]:
        resp += "(4,4)"
    resp += "}"
    resp += classe
    return resp




resposta=" "
arq = open('C:/Users/JoaoVitor/LmdTrabalhos/RelacoesBinarias.txt', 's')
for relacao in range (0, 65536):
    resposta = classifica(relacao) + arq.write(resposta)