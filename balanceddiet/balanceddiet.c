
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int bits[21];

int cache[1<<20]={-1};

void init_bits() {
	bits[0]=1;
	int i;
	for (i=1;i<21;i++) {
		bits[i]=bits[i-1]<<1;
	}
}

void init_cache(int *cans,int n) {
	int i;
	for (i=0;i<n;i++) {
		cache[bits[i]]=cans[i];
	}
}


void clear_cache() {
	int i;
	for (i=0;i<bits[20];i++) {
		cache[i]=-1;
	}
}


int getsum(int descriptor,int *cans) {
	if (cache[descriptor]>=0) {
		return cache[descriptor];
	}
	if (!descriptor) {
		cache[0]=0;
		return 0;
	}
	int rbit= (descriptor&-descriptor);
	cache[descriptor]=cache[rbit]+getsum(descriptor-rbit,cans);
	return cache[descriptor];
}


int optimize(int descriptor,int index,int * cans,
	int numcans,int target) {
	int m0,m1,temp;
	if (index==numcans) {
		return getsum(descriptor,cans);
	}
	m0=optimize(descriptor,index+1,
		cans,numcans,target);
	m1=optimize(descriptor+bits[index],index+1,
		cans,numcans,target);
	if (m0>m1) {
		temp=m0;
		m0=m1;
		m1=temp;
	}
	if (abs(target-m0)<=abs(target-m1)) {
		return m0;
	}
	return m1;
}


void read_can(int * cans, int n) {
	int i;
	for (i=0;i<n;i++) {
		scanf("%d",&cans[i]);
	}

}

int max(int x,int y) {
	return x>y? x:y;
}

int min(int x,int y) {
	return x<y? x:y;
}


int main(int argc, char const *argv[])
{
	init_bits();
	clear_cache();
	int n,cals,temp,s;
	int cans[20];
	scanf("%d",&n);
	while (n) {
		//printf("%d\n", n);
		read_can(cans,n);
		init_cache(cans,n);
		s=getsum(bits[n]-1,cans);
		cals=optimize(0,0,cans,n,s/2);
		printf("%d %d\n",max(cals,s-cals),min(cals,s-cals) );
		scanf("%d",&n);
		clear_cache();
	}
	return 0;
}





