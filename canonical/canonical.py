

def get_maxc():
    maxc = [-1]*(limit+1)
    maxc[0] = 0
    curr =-1
    for j in xrange(1,limit+1):
        if curr+1<len(coins) and coins[curr+1]<=j:
            curr+=1
        maxc[j] = curr
    return maxc


def greedy(i):
    count =0
    while i:
        # print i
        inc,i =divmod(i,coins[maxc[i]])
        count+=inc
        # print i
    return count



n= map(int, raw_input().split())

coins= map(int, raw_input().split())


limit = sum(coins[-2:])

maxc = get_maxc()
# print maxc

dp = [-1]*(limit+1)
dp[0] =0

for i in xrange(1,limit):
    ans = float('inf')
    for j in coins:
        if j>i:
            break
        ans = min(ans, 1+dp[i-j])
    dp[i] = ans

# print dp

for i in xrange(limit):
    if greedy(i)>dp[i]:
        print 'non-canonical'
        break
else:
    print 'canonical'
