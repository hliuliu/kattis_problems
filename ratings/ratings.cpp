

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef long long LL;


LL choose(LL n, LL r) {
	if (r<0 || r>n) {
		return 0;
	}
	if ((r<<1)>n) {
		r = n-r;
	}
	LL ans =1;
	for(LL i =1;i<=r;i++,n--) {
		ans *= n;
		ans /= i;
	}
	return ans;
}

LL compute(VI &ratings) {
	VI Rsum (1,0);
	for (int r: ratings) {
		Rsum.push_back(r+Rsum.back());
	}

	int s = Rsum.back(), n = ratings.size();
	LL ans = choose(s+n-1,n)+1;

	for (int i=1;i<=n;i++) {
		int k = s-Rsum[i-1];
		ans += choose(k+n-i,k);
		k= s-Rsum[i];
		ans -= choose(k+n-i,k);
	}

	return ans;
}


int main(int argc, char const *argv[])
{
	while (1) {
		int n;
		cin >> n;
		if (!n) {break;}
		VI ratings(n);
		for (int &r : ratings) {
			cin >> r;
		}
		cout << compute(ratings) << endl;
	}
	return 0;
}



