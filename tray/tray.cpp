

#include <iostream>
#include <bitset>

using namespace std;

bitset<72> layout, badpos;
int m;

int mask(double a, double b) {return (int)(a)*m+(int)(b);}

void track(int pos, int &count) {
	if (pos>=3*m) {
		count++;
		// cout << layout << endl;
	}else {
		if (layout[pos] || badpos[pos]) {
			track(pos+1,count);
		}else {
			layout[pos] = 1;
			track(pos+1,count);
			if ((pos+1)%m) {
				if (!(layout[pos+1] || badpos[pos+1])) {
					layout[pos+1] = 1;
					track(pos+2, count);
					layout[pos+1] = 0;
				}
			}
			if (pos<2*m) {
				if (!(layout[pos+m] || badpos[pos+m])) {
					layout[pos+m] = 1;
					track(pos+1, count);
					layout[pos+m] = 0;
				}
			}
			layout[pos] = 0;
		}
	}
}


int main() {
	int n;
	float x,y;
	cin >> m >> n;
	while(n--) {
		cin >> x >> y;
		badpos[mask(y,x)] = 1;
	}
	int count = 0;
	track(0, count);
	// cout << layout << badpos << endl;
	cout << count << endl;
	return 0;
}

