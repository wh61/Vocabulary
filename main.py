import string
import math

def filter(long_string):
	delList = string.punctuation+" '《》（）&%￥#@！{}【】？。，—_“”：；、<>"
	t = long_string.maketrans(delList, ''*len(delList))
	stringList = long_string.translate(t)
	return stringList3

def findPos(clean_string):

    return posList

def calDOF(dic):
	freq = dic.values()
	sumOfFreq = sum(freq)
	func = lambda x: -x/sumOfFreq*math.log(x/sumOfFreq)
	return sum(list(map(func, freq)))

def calFreqAndrightDOF(clean_string, posList, DigLen):
	
	freqDic = {}
	RDOFdic = {}
	length = len(clean_string)
	for m in range(1, DigLen+1):
		for i in posList:
			if i > length - m:
				continue
			else:
				target = clean_string[i:i+m]
				if target not in freqDic:
					freqDic[target] = 1
					RDOFdic[target] = {}
					if i >= length + m:
						continue
					else:
						RDOFdic[target][clean_string[i+m]] = 1
				else:
					freqDic[target] += 1
					if i >= length + m:
						continue
					else:
						if clean_string[i+m] not in RDOFdic[target]:
							RDOFdic[target][clean_string[i+m]] = 1
						else:
							RDOFdic[target][clean_string[i+m]] += 1
	RDOF = {}
	DOC = {}
	for key in RDOFdic:
		RDOF[key] = calDOF(RDOFdic[key])
		if len(key) == 1:
			DOC[key] = 0
		elif len(key) == 2:
			if key[0] not in freqDic:
				DOC[key] = 0
				continue
			if key[1] not in freqDic:
				DOC[key] = 0
				continue
			DOC[key] = freqDic[key]*length/freqDic[key[0]]/freqDic[key[1]]
		elif DigLen > 2:
			tmp = 1000000
			for t in range(len(key)):
				key1 = key[0:t+1]
				key2 = key[t+1:]
				if key1 not in freqDic:
					DOC[key] = 0
					continue
				if key2 not in freqDic:
					DOC[key] = 0
					continue
				tmp = min(tmp, freqDic[key]*length/freqDic[key1]/freqDic[key2])
			DOC[key] = tmp
	return freqDic, RDOF, DOC

def calLeftDOF(clean_string, posList, DigLen):
	LDOFdic = {}
	length = len(clean_string)
	for m in range(1, DigLen+1):
		for i in posList:
			if i > length - m:
				continue
			else:
				target = clean_string[i:i+m]
				if target not in LDOFdic:
					LDOFdic[target] = {}
					if i >= length + m:
						continue
					else:
						LDOFdic[target][clean_string[i+m]] = 1
				else:
					if i >= length + m:
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

def calDOC():

    return



def main(DigLen):
	# DigLen表示最长码长
	#假定有5篇文本，命名一次为1.txt, 2.txt,...
	filename = ".txt"
	long_string = ""
	for i in range(5):
		f = open(str(i+1)+filename, 'r', encoding = "gbk")
		for line in f:
			if line[-1] == "\n":
				line = line[:-1]
			long_string += line
		f.close()

	#stringList = filter(long_string)

	posList = findPos(clean_string)
	freqDic, RDOF, DOC = calFreqAndrightDOF(clean_string, posList, DigLen)
	r_clean_string = clean_string[::-1]
	r_postList = findPos(r_clean_string)
	LDOF = calFreqAndrightDOF(r_clean_string, r_posList, DigLen)

	return 0

