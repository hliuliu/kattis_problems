

#include <iostream>
#include <string>

using namespace std;

int main() {
	int l,x,p,sz=0, deny =0;
	cin >> l >> x;
	string action;
	while(x--) {
		cin >> action;
		cin >> p;
		if (action =="enter") {
			if (sz+p>l) {
				deny++;
			}
			else {
				sz+=p;
			}
		}else{
			sz-=p;
		}
	}
	cout << deny << endl;
	return 0;
}

