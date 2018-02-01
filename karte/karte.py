


missing= dict(zip('PKHT',[13]*4))

def sep(line):
    if not line:
        return []
    return [line[:3]]+sep(line[3:])

cards=sep(raw_input())

if len(set(cards))<len(cards):
    print 'greska'.upper()

else:
    for t,x,y in cards:
        missing[t]-=1

    print ' '.join(map(str,(missing[t] for t in 'PKHT')))

