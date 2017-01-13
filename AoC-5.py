import md5, re
# m = md5.new('abc').hexdigest()
# index = 0
# # print md5.new(('abc'+str(12)).encode('utf-8')).hexdigest()
# password = ''
# while len(password) < 8:
# 	if md5.new('abbhdwsy'+str(index)).hexdigest()[:5] == "00000":
# 		print md5.new('abbhdwsy'+str(index)).hexdigest()
# 		password += md5.new('abbhdwsy'+str(index)).hexdigest()[5]

# 	index +=1
# print password
#part two
index = 0
# print md5.new(('abc'+str(12)).encode('utf-8')).hexdigest()
patternNum = re.compile('[0-7]')
positions= []
password = {}
actualPassword = ''

while len(password) < 8:
	hashie = md5.new('abbhdwsy'+str(index)).hexdigest()
	if hashie[:5] == "00000":
		# print hashie
		# print hashie[5]
		if patternNum.match(hashie[5]):
			# print "its a num"
			if hashie[5] not in password:
				password[hashie[5]]=hashie[6]
				positions.append((hashie[5],hashie[6]))


	index +=1
print password
print positions
print sorted(positions, key=lambda tup:tup[0])
for i in sorted(positions, key=lambda tup:tup[0]):
	actualPassword += i[1]
print actualPassword