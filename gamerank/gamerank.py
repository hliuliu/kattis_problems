
ranks = [0]+[5]*10+[4]*5+[3]*5+[2]*5

level = 25
stars = 0
conswin = 0

for c in raw_input():
	if level==0:
		break
	if c=='W':
		conswin+=1
		stars += 1
		if conswin>=3 and level>=6:
			stars += 1
		if stars>ranks[level]:
			stars -= ranks[level]
			level -= 1
	else:
		conswin = 0
		if level <=20:
			if stars>0:
				stars -=1
			else:
				if level <20:
					level +=1
					stars = ranks[level]-1


print {0:"Legend"}.get(level, level)



