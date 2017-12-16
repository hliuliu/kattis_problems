
// Accepted :)

#include <iostream>
#include <vector>
#include <set>
#include <iterator>
#include <unordered_set>
#include <utility>
#include <string>
#include <algorithm>

using namespace std;
typedef pair<int,int> PII;


int det(int a,int b, int c,int d) {
	return a*d-b*c;
}


char get_turn(int a, int b, int c, vector <PII> &pts) {
	int xa = pts[a].first, xb = pts[b].first, xc= pts[c].first;
	int ya = pts[a].second, yb = pts[b].second, yc= pts[c].second;
	return det(xc-xb,yc-yb,xb-xa,yb-ya)>0?'R':'L';
}

vector<int> matinv(int a, int b, int c, int d) {
	vector<int> ans;
	ans.push_back(d);
	ans.push_back(-b);
	ans.push_back(-c);
	ans.push_back(a);
	return ans;
}

vector<int> matmult(int a, int b, int c, int d, int x, int y) {
	vector<int> ans;
	ans.push_back(a*x+b*y);
	ans.push_back(c*x+d*y);
	return ans;
}


bool intersect(PII p1,PII p2,PII q1,PII q2) {
	int p1x = p1.first, p1y = p1.second;
	int p2x = p2.first, p2y = p2.second;
	int q1x = q1.first, q1y = q1.second;
	int q2x = q2.first, q2y = q2.second;
	int x = p2x-q2x;
	int y = p2y-q2y;
	int ma = p2x-p1x, mb=q1x-q2x, mc= p2y-p1y, md = q1y-q2y;
	int dem = det(ma,mb,mc,md);
	if (dem==0) {
		return false;
	}
	vector<int> minv = matinv(ma,mb,mc,md);
	vector<int> param = matmult(minv[0], minv[1], minv[2], minv[3], x, y);
	for (int par:param) {
		bool expr = dem<0? (par>0 || par<dem) : (par<0 || par>dem);
		if (expr) {
			return false;
		}
	}
	return true;
}


bool does_intersect(int i, vector<int>&perms, vector<PII> &pts) {
	for (int j=0;j<perms.size()-2;j++) {
		if (intersect(pts[perms[j]],pts[perms[j+1]], pts[perms.size()-1],pts[i])) {
			return true;
		}
	}
	return false;
}
 
bool trav( set<int> &unseen, vector<PII> &pts, vector<int> &perm, string &dirs) {
	int n = pts.size();
	if (unseen.empty()) {
		return true;
	}
	vector<int> togo(unseen.size());
	copy(unseen.begin(),unseen.end(),togo.begin());
	for (int i: togo) {
		if (perm.size()<2) {
			perm.push_back(i);
			unseen.erase(i);
			if (trav(unseen,pts,perm,dirs)) {
				return true;
			}
			unseen.insert(i);
			perm.pop_back();
		} else {
			int index = perm.size()-2;
			if (get_turn(perm[perm.size()-2],perm[perm.size()-1], i, pts) == dirs[index] && !does_intersect(i,perm,pts)) {
				perm.push_back(i);
				unseen.erase(i);
				if (trav(unseen,pts,perm,dirs)) {
					return true;
				}
				unseen.insert(i);
				perm.pop_back();
			}
		}
	}
	return false;
}

int main(int argc, char const *argv[])
{
	

	int n;
	cin >> n;

	vector <PII> pts (n);

	for (PII &p:pts) {
		cin >> p.first >> p.second;
	}

	string dirs = "";

	cin >> dirs;

	// set <int> seen, unseen;

	// for (int i=0;i<n;i++) {
	// 	unseen.insert(i);
	// }

	vector<int> perm;

	int best = 0;

	for (int i =0;i<n;i++) {
		if (pts[i]<pts[best]) {
			best = i;
		}
	}

	vector<bool> vis (n,false);

	vis [best] = true;
	perm.push_back(best);

	for (int i =0;i<n-2;i++) {
		int next = -1;
		char d = dirs[i];
		for (int j =0;j<n;j++) {
			if (!vis[j]) {
				if (next<0 || get_turn(best,next,j,pts)!=dirs[i]) {
					next = j;
				}
			}
		}
		best = next;
		vis[best] = true;
		perm.push_back(best);
	}

	for (int i =0;i<n;i++) {
		if(!vis[i]) {
			perm.push_back(i);
		}
	}

	for (int &v: perm) {
		v++;
	}

	copy(perm.begin(),perm.end(), ostream_iterator<int>(cout, " "));

	cout << endl;


	return 0;
}



