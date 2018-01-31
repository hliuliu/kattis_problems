

case = 1

while 1:
    try:
        cx,cy,r = map(float, raw_input().split())
    except:
        break
    else:
        c = complex(cx,cy)
        z = complex(0)
        r = int(r)
        for _ in xrange(r):
            z = z**2+c
            if abs(z)>2:
                break
        else:
            print 'Case {}: {}'.format(case, 'IN')
            case += 1
            continue
        print 'Case {}: {}'.format(case, 'OUT')
        case += 1



