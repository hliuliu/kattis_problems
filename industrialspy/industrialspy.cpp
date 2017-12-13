
#include <iostream>
#include <cmath>
#include <unordered_set>
#include <string>

using namespace std;
typedef unordered_set<int> usi;

usi primes;


bool isprime(int n) {
	if (n<2) {
		return false;
	}
	for (int i =2;i*i<=n;i++) {
		if (n%i==0) {
			return false;
		}
	}
	return true;
}


void gen(string digits, int used, int acc) {
	if (isprime(acc)) {
		primes.insert(acc);
	}
	if (used == (1<<digits.length())-1) {
		return;
	}

	for (int i=0;i<digits.length();i++) {
		if (used&(1<<i)) {continue;}
		acc *= 10;
		acc += (int)(digits[i])-(int)('0');
		used|=(1<<i);
		gen(digits,used,acc);
		used^=(1<<i);
		acc/=10;
	}
}


int main() {
	int c;
	cin >> c;
	string digits;
	while (c--) {
		cin >> digits;
		gen(digits,0,0);
		cout << primes.size() << endl;
		primes.clear();
	}
	return 0;
}




