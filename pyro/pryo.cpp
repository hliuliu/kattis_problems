

#include <iostream>
#include <vector>
#include <set>

using namespace std;

int nb (int x) {
	int ans =0;
	while (x) {
		if (ans==2) {
			return false;
		}
		x = x ^ (x&(-x));
		ans++;
	}
	return true;
}



int main(int argc, char const *argv[])
{
	vector<int> L;
	set<int> S;
	int n;
	cin >> n;
	while(n>=0) {
		L.push_back(n);
		S.insert(n);
		cin>>n;
	}
	for (int i =0;i<L.size();i++) {
		int count = 0, value = L[i];
		for (int j =0;j<20;j++) {
			int tmp = value ^ (1<<j);
			if (tmp>value && S.find(tmp)!=S.end()) {
				count++;
			}
			for (int k=0;k<j;k++) {
				int tmp2 = tmp ^ (1<<k);
				if (tmp2>value && S.find(tmp2)!=S.end()) {
					count++;
				}
			}
		}
		cout << L[i] << ":" << count << "\n";
	}
	return 0;
}




