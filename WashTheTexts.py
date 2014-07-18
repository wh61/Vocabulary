def charactor2Int(charactor):
        bys = charactor.encode('GBK')
        if (len(bys) != 2): return -1;
        if (not((bys[0] > 129 and bys[0] < 255) and
                        (bys[1] > 63 and bys[1] < 255 ))): return -1
        by0 = int(bys[0])
        by1= int(bys[1])
        hs = (by0 - 129) * 190 + (by1 - 64) - by1 // 128
        if (hs < 9026): return -1
        return hs - 9025

I2C = ["" for i in range(25000)]

def WashTheTexts_(fileName, int2charactor):
        arr = []
        f1 = open(f
                  ileName, 'r', encoding = 'GBK')
        inputStr = f1.read()
        ResultStr = ""
        for ch in inputStr:
                hashValue = charactor2Int(ch)
                if (hashValue < 0): continue
                arr.append(hashValue)
                ResultStr += ch
                int2charactor[hashValue] = ch
        return ResultStr


def WashTheTexts(fileName, int2charactor = I2C):
        return WashTheTexts_(fileName, I2C)

def getCharator(index, arr = I2C):
        return I2C[index]

arr = WashTheTexts("test_texts.txt")


