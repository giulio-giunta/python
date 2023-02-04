# Without string multiplication - Ugly solution

for num in range(1,11):
	count = 1
	smileys = ''
	while count <= num:
		smileys += '\U0001f600'
		print(smileys)
		count +=1

