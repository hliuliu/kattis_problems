
#include <stdio.h>
#include <stdlib.h>
#define MAX_N 10000

int seq[MAX_N];

int table[MAX_N+1][MAX_N+1];


int no_pair(int end, int val) {
	return table[val][end];
}


int dfs(int n, int end) {
	if (table[n][end]>=0) {
		return table[n][end];
	}
	if (end<3) {
		table[n][end] = 1;
		return 1;
	}
	if (dfs(n,end-1)) {
		table[n][end] = no_pair(end-1,seq[end-1]);
		return table[n][end];
	}
	table[n][end] = 0;
	return 0;
}

void init_table(int n) {
	int i,j,val,end;
	for (i=0;i<=n;i++) {
		table[n][i] = -1;
		if (i<n) {
			for (j=0;j<=n;j++) {
				table[i][j] = 1; // seq[0..end], i has no AP with i
			}
		}
	}

	for (i=0;i<n-1;i++) {
		for (j=i+1;j<n;j++) {
			end = j+1;
			val = 2*seq[j]-seq[i];
			if (val>=0 && val<n) {
				table[val][end] = 0; // seq[i],seq[j],val form AP
			}
		}
	}

	for (val=0;val<n;val++) {
		for (end=1;end<=n;end++) {
			// inserting elements after having AP, still reamains AP
			table[val][end] &= table[val][end-1];
		}
	}
}


int main(int argc, char const *argv[])
{
	int n,i,j,ans;
	scanf("%d", &n);
	while (n) {
		getchar();
		// printf("%d\n", n);
		
		// printf("ok\n");
		for (i=0;i<n;i++) {
			scanf("%d", &seq[i]);
		}
		init_table(n);
		ans =1 ;
		for(i=3;i<=n && (ans=dfs(n,i));i++);
		printf("%s\n", ans? "yes" : "no");
		scanf("%d", &n);
	}
	return 0;
}



