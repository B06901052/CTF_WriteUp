plain_text = '2229555555768432252223133777492611'
standard = plain_text[0]
count = 0
cipher = ''
for i in range(len(plain_text)):
	if(standard == plain_text[i]):
		count += 1
	else:
		cipher += str(count)
		cipher += standard
		standard = plain_text[i]
		count = 1
cipher += str(count)
cipher += standard
print(cipher)  # 3219651716181413221532131123371419121621
