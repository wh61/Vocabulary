#import string
import math

"""def filter(long_string):
	delList = string.punctuation+" '《》（）&%￥#@！{}【】？。，—_“”：；、<>"
	t = long_string.maketrans(delList, ''*len(delList))
	stringList = long_string.translate(t)
	return stringList3"""

I2C = ["" for i in range(25000)]

def charactor2Int(charactor):
        try:
                bys = charactor.encode('GBK')
        except:
                return -1;
        if (len(bys) != 2): return -1;
        if (not((bys[0] > 129 and bys[0] < 255) and
                        (bys[1] > 63 and bys[1] < 255 ))): return -1
        by0 = int(bys[0])
        by1= int(bys[1])
        hs = (by0 - 129) * 190 + (by1 - 64) - by1 // 128
        if (hs < 9026): return -1
        return hs - 9025

def WashTheTexts_(inputStr, int2charactor):
        arr = []
        ResultStr = ""
        for ch in inputStr:
                hashValue = charactor2Int(ch)
                if (hashValue < 0): continue
                arr.append(hashValue)
                ResultStr += ch
                int2charactor[hashValue] = ch
        return ResultStr


def WashTheTexts(inputStr, int2charactor = I2C):
        return WashTheTexts_(inputStr, I2C)

def getCharator(index, arr = I2C):
        return I2C[index]

def findPos(texts, d):
    s = texts
    strLen = len(s)
    for i in range(2 * (d + 1)): s += "ä¸"
    dic = {}
    for i in range(strLen):
        Str = ""
        for j in range(d + 1):
            Str += s[i + j]
        dic[Str] = i
    keyList = sorted(dic)
    pos = []
    for key in keyList:
        pos.append(dic[key])
    return pos

def calDOF(dic):
        #print(dic)
        #if len(dic) == 1:
        #        return 0
        freq = dic.values()
        sumOfFreq = sum(freq)
        func = lambda x: -x/sumOfFreq*math.log(x/sumOfFreq)
        return sum(list(map(func, freq)))

def calFreq_RDOF_DOC(clean_string, posList, DigLen):
	#print (clean_string, posList, DigLen)
	freqDic = {}
	RDOFdic = {}
	length = len(clean_string)
	for m in range(1, DigLen+1):
		for i in posList:
			if i+m > length:
				continue
			else:
				target = clean_string[i:i+m]
				#print ("target: ", target)
				#print ("length: ", length)
				#print ("i: ", i)
				#print ("m: ", m)
				if target not in freqDic:
					freqDic[target] = 1
					RDOFdic[target] = {}
					if i+m == length:
						continue
					else:
						RDOFdic[target][clean_string[i+m]] = 1
				else:
					freqDic[target] += 1
					if i+m == length:
						continue
					if clean_string[i+m] not in RDOFdic[target]:
						RDOFdic[target][clean_string[i+m]] = 1
					else:
						RDOFdic[target][clean_string[i+m]] += 1
	RDOF = {}
	DOC = {}
	#print(freqDic)
	for key in RDOFdic:
		RDOF[key] = calDOF(RDOFdic[key])
		#print (key)
		if len(key) == 1:
			DOC[key] = 1
		elif len(key) == 2:
			#if key[0] not in freqDic:
			#	DOC[key] = 0
			#	continue
			#if key[1] not in freqDic:
			#	DOC[key] = 0
			#	continue
			DOC[key] = freqDic[key]*length/freqDic[key[0]]/freqDic[key[1]]
		elif DigLen > 2:
			tmp = 1000000
			for t in range(len(key)-1):
				key1 = key[0:t+1]
				key2 = key[t+1:]
				#if key1 not in freqDic:
				#	DOC[key] = 0
				#	continue
				#if key2 not in freqDic:
				#	DOC[key] = 0
				#	continue
				tmp = min(tmp, freqDic[key]*length/freqDic[key1]/freqDic[key2])
			DOC[key] = tmp
	return freqDic, RDOF, DOC

def calLDOF(clean_string, posList, DigLen):
	LDOFdic = {}
	length = len(clean_string)
	for m in range(1, DigLen+1):
		for i in posList:
			if i + m > length:
				continue
			else:
				target = clean_string[i:i+m]
				if target not in LDOFdic:
					LDOFdic[target] = {}
					if i + m == length:
						continue
					else:
						LDOFdic[target][clean_string[i+m]] = 1
				else:
					if i + m == length:
						continue
					else:
						if clean_string[i+m] not in LDOFdic[target]:
							LDOFdic[target][clean_string[i+m]] = 1
						else:
							LDOFdic[target][clean_string[i+m]] += 1
	LDOF = {}
	for key in LDOFdic:
		LDOF[key] = calDOF(LDOFdic[key])
	return LDOF


def main(DigLen):
	# DigLen表示最长码长
	#假定有5篇文本，命名一次为1.txt, 2.txt,...
	filename = "gongchengche"
	long_string = ""
	#for i in range(1):
	#	f = open(filename, 'r', encoding = 'utf-8')
	#	for line in f:
	#		#print (line)
	#		#break
	#		if line[-1] == "\n":
	#			line = line[:-1]
	#		long_string += line
	#	f.close()
	f = open(filename, 'r', encoding = 'utf-8')
	long_string = f.read()
	f.close()
	#print(long_string)
	#long_string.decode('utf-8')
	clean_string = WashTheTexts(long_string)
	#stringList = filter(long_string)

	posList = findPos(clean_string, DigLen)
	freqDic, RDOF, DOC = calFreq_RDOF_DOC(clean_string, posList, DigLen)
	r_clean_string = clean_string[::-1]
	r_posList = findPos(r_clean_string, DigLen)
	LDOF = calLDOF(r_clean_string, r_posList, DigLen)
	#print ("freqDic: ", freqDic)
	#print ("RDOF: ", RDOF)
	#print ("LDOF: ", LDOF)
	#print ("DOC: ", DOC)
	for word in freqDic.keys():
                if freqDic(word) > 10:
                        if min(RDOF[word], LDOF[word]) > 0.5:
                                if DOC[word] > 0.5:
                                        print(word)	
                                
main(5)
