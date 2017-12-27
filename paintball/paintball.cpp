
// Accepted

#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

int targets [2001];
int n,m;
bool G[1001][1001];
bool visited[1001];


bool match_up(int i) {
	for (int j=1;j<=n;j++) {
		if (G[i][j] && !visited[j]) {
			visited[j] = true;
			if(targets[n+j]==0 || match_up(targets[n+j])) {
				targets[i] = n+j;
				targets[n+j] = i;
				return true;
			}
		}
	}
	return false;
}


bool attack () {
	int count =0;

	for (int i =1;i<=n;i++) {
		fill_n(visited,n+1,false);
		if (match_up(i)) count ++;
	}

	return count == n;
}

int main(int argc, char const *argv[])
{
	fill_n(targets,2001, 0);
	cin >> n >> m;

	int a,b;

	for (int i =0;i<1001;i++) {
		fill_n(G[i],1001, false);
	}

	for (int i =0;i<m;i++) {
		cin >> a >> b;
		G[a][b] = true;
		G[b][a] = true;
	}

	if (attack()) {
		for (int i =1;i<=n;i++) {
			cout << targets[i]-n << endl;
		}
	}else {
		cout << "Impossible" << endl;
	}

	return 0;
}

