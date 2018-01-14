
#include <iostream>
#include <vector>

#define MOD 1000000007

using namespace std;
typedef vector<int> ivec;
typedef vector<ivec> imat;
typedef long long LL;

imat A = {{1,1},{1,0}};
imat ident = {{1,0},{0,1}};

imat matmult(imat A, imat B) {
	imat C(2,ivec(2));
	for (int i =0;i<2;i++) {
		for (int j=0;j<2;j++) {
			LL res = 0;
			for (int k =0;k<2;k++) {
				res += (LL)(A[i][k])*B[k][j];
				res %= MOD;
			}
			C[i][j] = (int) (res);
		}
	}
	return C;
}

imat matexp(imat A, int n) {
	if (n==0) {return ident;}
	if (n==1) {return A;}
	imat B =  matexp(A,n>>1);
	B= matmult(B,B);
	if (n&1) {B= matmult(B,A);}
	return B;
}

int fib(int n) {
	if (n<2) {return n;}
	return matexp(A,n)[0][0];
}



int main() {
	int t,n;
	cin >>t;
	while (t--) {
		cin >>n;
		cout << fib(n+1) << endl;
	}
	return 0;
}

