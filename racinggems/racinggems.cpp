
// Accepted :)

#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <utility>
#include <cmath>

using namespace std;

typedef unsigned int uint;

int r;




void transform_(int r, pair<long,long> &gem) {
	long x = gem.first, y= gem.second;
	gem.first = x*r+y;
	gem.second = y-x*r;
}


int binsearch(long key, vector<int> &tail, vector<long> &arr, int start, int end) {
	while (end-start>2) {
		int mid = (start+end)/2;
		if (arr[tail[mid]]>key) {
			end = mid + 1;
		}
		else {
			start = mid+1;
		}
	}
	if (arr[tail[start]]>key) {
		return start;
	}
	return start+1;
}


int LIS (vector<long> &arr) {
	int n = arr.size();
	vector <int> tail(n,0);//prev(n,-1);
	int sz =1;
	for (int i =1;i<n;i++) {
		if(arr[i]<arr[tail[0]]) {
			tail[0]=i;
		}
		else if (arr[i]>=arr[tail[sz-1]]) {
			// prev[i] = tail[sz-1];
			tail[sz++] = i;
		}else {
			int j = binsearch(arr[i],tail,arr, 1, sz);
			// prev[i] = tail[j-1];
			tail[j] = i;
		}
	}
	return sz;
}


int main(int argc, char const *argv[])
{
	int n,w,h;
	cin >> n >> r >> w >> h;
	vector<pair<long,long> > gems (n);
	for (int i=0;i<n;i++) {
		cin >> gems[i].first >> gems[i].second;
		transform_(r,gems[i]);
		// cout << gems[i].first << " " << gems[i].second << endl;
	}
	sort(gems.begin(),gems.end());
	// cout << endl;
	vector<long> arr(n);
	for (int i =0;i<n;i++) {
		// cout << gems[i].first << " " << gems[i].second << endl;
		arr[i] = gems[i].second;
	}
	int ans = LIS(arr);
	cout << ans << "\n";
	return 0;
}



