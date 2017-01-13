import re, collections

pattern = re.compile('[^a-zA-z]')
patternNum = re.compile('[^0-9]')
#list of tupples of the 5 most common letters
def getCommonLetters(encname):
	return sorted(collections.Counter(pattern.sub('', encname.strip()[:-7])).most_common(), key=lambda x:(-x[1],x[0]))[:5]

def getChecksum(encname):
	return pattern.sub('',encname.strip()[-7:])

def getId(encname):
	return int(patternNum.sub('', encname))

def isItReal(commonLetters, checksum):
	print checksum
	print commonLetters
	for char in commonLetters:
		if char[0] not in checksum:
			return False
	return True	

def getSumID():
	idSum = 0
	file = open('AoC-4-input.txt', 'r')
		for line in file:
			if(isItReal(getCommonLetters(line), getChecksum(line))):
				idSum += getId(line)
	return idSum

def letterRotator(char, shift):
	if(ord(char)+shift > ord('z')):
		return chr(ord(char)+shift-26)
	else:
		return chr(ord(char)+ shift)

def decodeFile():
	file = open('AoC-4-input.txt', 'r')
	file2 = open('AoC-4-decoded.txt', 'w')
	for line in file:
		decoded = ""
		shift = getId(line)%26
		for char in line:
			if(not pattern.match(char)):
				decoded += letterRotator(char, shift)
			else:
				decoded+=char
		file2.write(decoded+'\n')

getSumID()
decodeFile()
