import string
import re

def filter(long_string):
	delList = string.punctuation+" '《》（）&%￥#@！{}【】？。，—_“”：；、<>"
	t = long_string.maketrans(delList, ' '*len(delList))
	stringList = long_string.translate(t)
	return stringList.split()

def findPos(short_string):

    return posList

def calFreq():

    return
def calDOF():

    return

def calDoc():

    return



def main():
	#假定有5篇文本，命名一次为1.txt, 2.txt,...
	filename = ".txt"
	for i in range(5):
		f = open(str(i+1)+filename, 'r', encoding = "gbk")
		long_string = ""
		for line in f:
			long_string += line
		stringList = filter(long_string)
		for short_string in stringList:
			posList = findPos(short_string)


    return 0
