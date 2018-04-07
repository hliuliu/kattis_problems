



notes = 'A, A#, B, C, C#, D, D#, E, F, F#, G, G#'.split(', ')
pattern = [2,2,1,2,2,2,1]
n=len(notes)


def scale(index):
	index %= n
	sc = [notes[index]]
	for pa in pattern:
		index =(index + pa)%n
		sc.append(notes[index])
	return sc



k = int(raw_input())

song = raw_input().split()
song=set(song)

print (lambda x: x if x else 'none')(' '.join([notes[i] for i in xrange(n) if song.issubset(set(scale(i)))]) )


