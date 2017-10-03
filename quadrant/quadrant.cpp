
#include <iostream>

using namespace std;


int quad(int x,int y) {
	return x>0? (y>0? 1 : 4) : (y>0? 2 : 3 );
}



int main() {
	int x,y;
	cin >> x;
	cin >> y;
	cout << quad(x,y) << endl;
	return 0;
}


