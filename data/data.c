
#include <stdio.h>
#include <stdlib.h>
#define MAX(a,b) ((a)>(b))? (a) : (b)

int si[15];
int sieve[1401];
int distinctpf[1401];
int partition[15];
int numparts[15];
int sprops[15];


int revenue(int * si,int n) {
	int i,ans;
	// for (i=0;i<n;i++) {
	// 	sprops[i]=0;
	// }
	// for (i=0;i<n;i++) {
	// 	sprops[partition[i]]+=si[i];
	// }
	ans=0;
	for (i=0;i<numparts[n-1];i++) {
		ans+=distinctpf[sprops[i]];
	}
	return ans;
}

int next_partition(int index) {
	if (index==0) {
		return 0;
	}
	if (partition[index]==numparts[index-1]) {
		if (!next_partition(index-1)) {
			return 0;
		}
		sprops[partition[index]]-=si[index];
		partition[index]=0;
		sprops[partition[index]]+=si[index];
		numparts[index]=numparts[index-1];
		return 1;
	}
	sprops[partition[index]]-=si[index];
	partition[index]++;
	sprops[partition[index]]+=si[index];
	if (numparts[index]==partition[index]) {
		numparts[index]++;
	}
	return 1;
}

void print_partition(int n) {
	int i;
	for (i=0;i<n;i++) {
		printf("%d ",partition[i]);
	}
	printf("\n");
}



int main(int argc, char const *argv[])
{
	int n,i,j,ans,rev;
	scanf("%d",&n);
	for(i=0;i<n;i++) {
		scanf("%d",&si[i]);
	}
	sieve[0]=0;
	sieve[1]=0;
	for(i=2;i<1401;i++) {
		sieve[i]=1;
	}
	for (i=0;i*i<1401;i++) {
		if (!sieve[i]) {
			continue;
		}
		for (j=i*i;j<1401;j+=i) {
			sieve[j]=0;
		}
	}
	for (i=1;i<1401;i++) {
		distinctpf[i]=0;
	}
	for (i=2;i<1401;i++) {
		if (!sieve[i]) {
			continue;
		}
		for(j=i;j<1401;j+=i) {
			distinctpf[j]++;
		}
	}
	for(i=0;i<15;i++) {
		partition[i] = 0;
		numparts[i] = 1;
	}

	for ( i=0; i<n;i++) {
		sprops[0]+=si[i];
		if (i>0) {
			sprops[i]=0;
		}
	}
	ans = revenue(si,n);
	// printf("%d\n", ans);
	// print_partition(n);

	while (next_partition(n-1)) {
		rev = revenue(si,n);
		// printf("%d\n", rev);
		// print_partition(n);
		ans = MAX(ans,rev);
	}
	printf("%d\n", ans);
	return 0;
}

