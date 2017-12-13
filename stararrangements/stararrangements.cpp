
#include <iostream>

using namespace std;


int main() {
	int s;
	cin >> s;
	cout << s << ':' << endl;
	for (int i =2;i-1<=(s>>1);i++ ) {
		int j = s % (2*i-1);
		if (j==0 || j==i ) {
			cout << i << "," << i-1 << endl;
		}
		j = s % (2*i);
		if (j==0 || j==i) {
			cout << i << "," << i << endl;
		}
	}
	return 0;
}


