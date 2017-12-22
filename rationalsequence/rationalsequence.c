
#include <stdio.h>
#include <stdlib.h>


int gcd(int a,int b) {
	int temp,r;
	if (a<b) {
		temp=a;
		a=b;
		b=temp;
	}
	while (b) {
		r=a%b;
		a=b;
		b=r;
	}
	return a;
}


int findn(int p,int q) {
	if (p==q) {
		return 1;
	}
	if (p<q) {
		return 2*findn(p,q-p);
	}
	return 2*findn(p-q,q)+1;
}


void getfrac(int n,int *p,int *q) {
	if (n==1) {
		*p=1;
		*q=1;
	}
	else {
		getfrac(n>>1,p,q);
		if (n&1) {
			*p+=*q;
		}else {
			*q+=*p;
		}
	}
}

void nxt (int *p,int *q) {
	if (*p<*q) {
		*q-=*p;
		*p+=*q;
	}else {
		*p-=*q;
		nxt(p,q);
		*q+=*p;
	}
}

int main(int argc, char const *argv[])
{
	int t,k,p,q,i,n;

	scanf("%d", &t);

	for (i=0;i<t;i++) {
		scanf("%d %d/%d", &k, &p ,&q );
		nxt(&p,&q);
		printf("%d %d/%d\n",k,p,q);
	}

	return 0;
}

