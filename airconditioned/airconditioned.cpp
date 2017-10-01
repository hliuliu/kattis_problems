
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



bitset<100> minions_pos;


bool in_interval(int val ,pair<int,int> itv) {
	return val >= itv.first && val <= itv.second;
}



set< pair<int,int> > simplify( set< pair<int,int> > minions) {
	set< pair<int,int> > :: iterator it1,it2,tmp;
	vector<bool> found (minions.size());
	int i,j;

	// set<list<pair<int,int> >:: iterator > toerase;

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


	

	// cout << minions.size() <<endl;

	// for (j=0; j<found.size();j++) {
	// 	cout << j << " " << found[j] << endl;
	// }

	// for (i=0;i<*n;i++) {
	// 	if (!found[i]) {
	// 		// cout << "i=" << i <<endl;
	// 		minions.push_back(minions_copy[i]);
	// 	}
	// }

	// i=0;

	// for (it1=minions.begin();it1!=minions.end();i++) {
	// 	if (found[i]) {
	// 		it1 = minions.erase(it1);
	// 	}else {
	// 		++it1;
	// 	}
	// }

	// *n = minions.size();

	return minions;

}


int minrooms(int start, int end, vector< pair<int,int> > minions, int count, int endpts[][2]) {
	if (start>end) {
		// all minions should be satisfied
		// for (int i= 0; i<minions.size();i++) {

		// }
		return minions_pos.count() == minions.size()? count : -1;
	}

	if (minions_pos.count()==minions.size()) {
		return count;
	}

	// don't use start temperature
	int ans0 = minrooms(start+1, end, minions, count, endpts);

	if (endpts[start][0]<0) {
		return ans0;
	}

	// now use it
	int ans1=0;

	int right = endpts[start][1];

	int left = endpts[start][0];

	while (left<=right && minions_pos.test(left)) {left++;}
	if (right<left) {
		return ans0;
	}

	for (int i =left;i<=right;i++) {
		minions_pos.set(i);
	}

	ans1 = minrooms(start+1,end, minions,count+1, endpts);

	for (int i =left;i<=right;i++) {
		minions_pos.set(i,0);
	}

	if (ans0<0) {
		return ans1;
	}

	if (ans1<0) {
		return ans0;
	}

	return min(ans0,ans1);
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

	// cout << n << endl;

	pair<int, int> interval;

	set< pair<int,int> > minions;

	for (int i=0;i<n;i++) {
		cin >> interval.first;
		cin >> interval.second;
		minions.insert(interval);
		// cout << interval.first << interval.second << endl;
	}

	minions =simplify( minions);

	n = minions.size();

	// cout << n << endl;

	// for(set<pair<int,int> >::iterator it = minions.begin();it!=minions.end();++it) {
	// 	cout << it->first << " " << it->second << endl;
	// }

	vector< pair<int,int> > minion_vec(n);

	copy(minions.begin(),minions.end(),minion_vec.begin());
	sort(minion_vec.begin(),minion_vec.end(),compare);

	int minion_endpts [201][2];
	for (int i =1; i<=2*m;i++) {
		minion_endpts[i][0] = -1;
		minion_endpts[i][1] = -1;
	}

	for (int j =0;j<n;j++) {
		for (int i=minion_vec[j].first;i<=minion_vec[j].second;i++) {
			if (minion_endpts[i][0]<0) {
				minion_endpts[i][0] = j;
			}
			minion_endpts[i][1]=j;
		}
	}


	cout << minrooms(1,2*m,minion_vec, 0, minion_endpts)<<endl;

	return 0;
}


