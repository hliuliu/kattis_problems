

n= int(raw_input())

univ, teams = set(), []

while n:
	n-=1
	line = raw_input()
	school = line.split()[0]
	if school not in univ:
		univ.add(school)
		teams.append(line)

print '\n'.join(teams[:12])



