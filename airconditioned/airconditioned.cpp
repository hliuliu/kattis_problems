
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <deque>
#include <utility>
#include <bitset>
#include <iterator>

using namespace std;



bitset<100> minions_pos;


bool in_interval(int val ,pair<int,int> itv) {
	return val >= itv.first && val <= itv.second;
}



void simplify(int * n, set< pair<int,int> > minions) {
	set< pair<int,int> > :: iterator it1,it2,tmp;
	bool found;

	for (it1 = minions.begin(); it1!=minions.end();) {
		found = false;
		for (it2 = minions.begin(); it2!=minions.end(); ++it2) {
			if (it1!=it2) {
				if (in_interval(it1->first,*it2) && in_interval(it1->second,*it2)) {
					tmp = it1;
					++tmp;
					minions.erase(it1);
					it1= tmp;
					found = true;
					(*n)--;
					break;
				}
			}
		}
		if (!found) {
			++it1;
		}
	} 
}


int minrooms(int start, int end, vector< pair<int,int> > minions, int count) {
	if (start>end) {
		// all minions should be satisfied
		// for (int i= 0; i<minions.size();i++) {

		// }
		return minions_pos.count() == minions.size()? count : -1;
	}

	// don't use start temperature
	int ans0 = minrooms(start+1, end, minions, count);

	// now use it
	int ans1=0;
	vector<int> new_accom;
	for (int i =0;i<minions.size();i++) {
		if (!minions_pos.test(i) && in_interval(start, minions[i])) {
			new_accom.push_back(i);
			minions_pos.set(i);
		}
	}

	ans1 = minrooms(start+1,end, minions,count+1);

	for (vector<int>::iterator it = new_accom.begin();it!=new_accom.end(); ++it ) {
		minions_pos.set(*it, 0);
	}


	if (ans0<0) {
		return ans1;
	}

	if (ans1<0) {
		return ans0;
	}

	return min(ans0,ans1);
}



int main(int argc, char const *argv[])
{
	
	int n,m;

	cin >> n;
	m=n;

	// cout << n << endl;

	pair<int, int> interval;

	set< pair<int,int> > minions;

	for (int i=0;i<n;i++) {
		cin >> interval.first;
		cin >> interval.second;
		minions.insert(interval);
		// cout << interval.first << interval.second << endl;
	}

	simplify(&n, minions);

	vector< pair<int,int> > minion_vec(n);

	copy(minions.begin(),minions.end(),minion_vec.begin());
	cout << minrooms(1,2*m,minion_vec, 0)<<endl;

	return 0;
}


