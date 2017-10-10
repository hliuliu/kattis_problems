
// TLE?

#include <iostream>
#include <utility>
#include <vector>
#include <list>
#include <set>
#include <algorithm>
#include <iterator>
#include <limits>
#include <map>
#include <cmath>
#include <deque>

using namespace std;

double dist(pair<int,int> &p, pair <int,int> &q);

class vertex {
	
public:
	int x,y,s,index;
	vertex(int vx, int vy, int vs) {
		x = vx;
		y = vy;
		s = vs;
	}
	bool operator==(vertex other) {
		return x == other.x && y == other.y;
	}
};

class edge {
public:
	vertex *u,*v;
	double wt;
	edge(vertex *eu, vertex *ev) {
		u = eu, v = ev;
		pair<int,int> a(u->x,u->y),b(v->x,v->y);
		wt = dist(a,b);
	}
};

class uf {
	vector<int> pid, sz;
public:
	uf(int n) {
		for (int i =0;i<n;i++) {
			pid.push_back(i);
			sz.push_back(1);
		}
	};

	int find(int i) {
		while (pid[i]!=i) {
			pid[i] = pid[pid[i]];
			i = pid[i];
		}
		return i;
	};
	void union_(int p,int q) {
		int i = find(p), j = find(q);
		if (i==j) {return;}
		if (sz[i]<sz[j]) {
			pid[i] = j;
			sz[j]+=sz[i];
		}else {
			pid[j]=i;
			sz[i]+=sz[j];
		}
	};

	bool connected(int p, int q) {
		return find(p)==find(q);
	}

};

vector<vertex> V;
vector<edge> E;


/*bool next_perm(vector <int> &perm) {
	int n = perm.size();
	int i,j;
	i =n-1;
	while (i>0 && perm[i]<perm[i-1]) {
		i--;
	}
	if (i==0) {
		return false;
	}
	vector<int> :: iterator itr;
	itr = min_element(perm.begin()+i, perm.end());
	j = itr - perm.begin();
	// cout << i << " " << j << endl;
	swap(perm[i-1],perm[j]);

	sort(perm.begin()+i,perm.end());
	return true;
}*/

bool next_perm(deque <int> &perm, vector<bool> &dirs,int ctr) {
	if (ctr==0) {
		return false;
	}
	int index = find(perm.begin(),perm.end(),ctr)-perm.begin();
	if (!dirs[ctr]) {
		if (index>0) {
			swap(perm[index],perm[index-1]);
			return true;
		}
		dirs[ctr] = true;
		perm.pop_front();
		if (!next_perm(perm,dirs,ctr-1)) {
			perm.push_front(ctr);
			return false;
		}
		perm.push_front(ctr);
		return true;
	}
	if (index<ctr) {
		swap(perm[index],perm[index+1]);
		return true;
	}
	dirs[ctr] = false;
	perm.pop_back();
	if (!next_perm(perm,dirs,ctr-1)) {
		perm.push_back(ctr);
		return false;
	}
	perm.push_back(ctr);
	return true;
}

double dist(pair<int,int> &p, pair <int,int> &q) {
	return sqrt(pow(q.first -p.first,2)+pow(q.second -p.second, 2));
}

double compute(deque<int> &perm, vector<int> hide_time, vector<pair<int,int> > mice, double m) {
	int n = hide_time.size();
	pair<int,int> currp (0,0);
	double u =0.0, ratio = 0.0, mpow = 1.0;
	for (int i=0;i<n;i++) {
		double d = dist(currp,mice[perm[i]]);
		u += d/mpow;
		mpow *= m;
		ratio = max(u/hide_time[perm[i]], ratio);
		currp=mice[perm[i]];
	}
	return ratio;
}

bool edgecmp(edge e1, edge e2) {
	vertex *u1,*v1,*u2,*v2;
	u1 = e1.u, v1 = e1.v;
	u2 = e2.u, v2 = e2.v;

	if (u1->s > v1->s) {
		swap(u1,v1);
	}

	if (u2->s > v2->s) {
		swap(u2,v2);
	}

	if (v1->s < u2-> s) {
		return true;
	}
	if (v1->s == u2->s) {
		if (u1->s== v2->s) {
			return e1.wt < e2.wt;
		}
		return true;
	}
	if (u2->s<u1->s) {
		return false;
	}
	if (u1->s==u2->s) {
		if (v1->s<v2->s) {
			return true;
		}
		if (v1->s==v2->s) {
			return e1.wt<e2.wt;
		}
		return false;
	}

	return true;
}

int get_next_vertex(int v, vector<edge> tree, vector<bool> &visited) {
	for (int i =0;i<tree.size();i++) {
		cout << tree[i].u->index << " " << tree[i].v->index << endl;
		if (!visited[i]) {
			if (tree[i].u->index == v) {
				visited[i] = true;
				return tree[i].v->index;
			}
			if (tree[i].v->index == v) {
				visited[i] = true;
				return tree[i].u->index;
			}
		}
	}
	return -1;
}

void mst(vector<int> &perm, vector<int> hide_time, vector<pair<int,int> > mice) {
	int n = mice.size();
	vertex * vref;
	vref = new vertex (0,0,0);
	vref->index = 0;
	V.push_back(*vref);
	for (int i =0;i<n;i++) {
		vref = new vertex (mice[i].first,mice[i].second,hide_time[i]);
		vref->index = i+1;
		V.push_back(*vref);
	}
	edge * eref;
	for (int i=0;i<=n;i++) {
		for (int j=0;j<i;j++) {
			eref =  new edge (&V[i],&V[j]);
			E.push_back(*eref);
		}
	}
	sort(E.begin(),E.end(), edgecmp);
	// for (int i =0;i<=n;i++) {
	// 	perm.push_back(-1);
	// }
	vector<edge> tree;
	uf comp (n+1);

	for (vector<edge>::iterator eit = E.begin();eit<E.end();++eit) {
		if (tree.size()==n) {
			break;
		}
		if (!comp.connected(eit->u->index,eit->v->index)) {
			tree.push_back(*eit);
			comp.union_(eit->u->index,eit->v->index);
		}
	}
	int vi=0;
	vector <bool> visited (tree.size());
	for (vector<bool>::iterator vit = visited.begin(); vit!=visited.end();++vit) {
		*vit = false;
	}
	cout << tree.size() << endl;
	for (int i =0;i<n;i++) {
		vi = get_next_vertex(vi, tree, visited);
		perm.push_back(vi-1);
	}

	
}


void print_perm(vector<int> perm) {
	for (vector<int>::iterator it = perm.begin(); it!=perm.end();++it) {
		cout << *it << " ";
	}
	cout << endl;
}

int main(int argc, char const *argv[])
{
	int n,x,y,s;
	double m;

	cin >> n;

	vector<pair<int,int> > mice;
	vector<int> hide_time;
	deque<int> perm;

	for (int i =0;i<n;i++) {
		cin >> x;
		cin >> y;
		cin >> s;
		mice.push_back(make_pair(x,y));
		hide_time.push_back(s);
		perm.push_back(i);
	}

	cin >> m;

	double minv= numeric_limits<double>::infinity();

	vector<bool> dirs (n);

	for (vector<bool>::iterator it = dirs.begin(); it!=dirs.end();++it) {
		*it = false; // for left
	}

	do {
		minv = min(minv, compute(perm,hide_time,mice,m));
		// print_perm(perm);
	} while (next_perm(perm,dirs,n-1));
	
	// mst(perm,hide_time,mice);
	// print_perm(perm);

	// minv = compute(perm,hide_time,mice,m);


	cout.precision(17);

	cout << fixed << minv << endl;

	return 0;
}



