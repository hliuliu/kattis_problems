


/// Accepted :) [finally]


#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <deque>
#include <utility>
#include <bitset>
#include <iterator>
#include <list>

using namespace std;




bool in_interval(int val ,pair<int,int> itv) {
	return val >= itv.first && val <= itv.second;
}



set< pair<int,int> > simplify( set< pair<int,int> > minions) {
	set< pair<int,int> > :: iterator it1,it2,tmp;
	vector<bool> found (minions.size());
	int i,j;

	vector< pair<int,int> > minions_copy (minions.size());
	copy(minions.begin(),minions.end(),minions_copy.begin());
	minions.clear();

	

	for (i=0;i<minions_copy.size();i++) {
		found[i] =false;
		for (j=0;j<minions_copy.size();j++) {
			if (i!=j && in_interval(
				minions_copy[j].first,minions_copy[i]) && in_interval(
				minions_copy[j].second,minions_copy[i]) ) {
				found[i] = true;
				break;
			}
		}
		if (!found[i]) {
			minions.insert(minions_copy[i]);
		}
	}


	return minions;

}



bool compare(pair<int,int> a,pair<int,int> b) {
	if (a.first!=b.first) {
		return b.first>a.first;
	}
	return b.second>a.second;
}

int main(int argc, char const *argv[])
{
	
	int n,m;

	cin >> n;
	m=n;


	pair<int, int> interval;

	set< pair<int,int> > minions;

	for (int i=0;i<n;i++) {
		cin >> interval.first;
		cin >> interval.second;
		minions.insert(interval);
		
	}

	minions =simplify( minions);

	n = minions.size();


	vector< pair<int,int> > minion_vec(n);

	copy(minions.begin(),minions.end(),minion_vec.begin());
	sort(minion_vec.begin(),minion_vec.end(),compare);


	int start = 0, ans = 0;
	while (start<n) {
		int room = minion_vec[start].second;
		ans++;
		for (;start<n && in_interval(room, minion_vec[start]);start++) {}
	}

	cout << ans << endl;

	return 0;
}


