
#include <stdio.h>
#include <stdlib.h>

typedef struct pair {
	int k,v;
} pair;

int bits[25];

int mdir[2][2]={{0,1},{1,0}};

int inbound(int m, int x, int y) {
	return x>=0 && x<3 && y>=0 && y<m;
}


pair* nextcoords(int m,int x,int y){
	pair * pptr=malloc(sizeof(pair));
	if (y==m-1) {
		pptr->k=x+1;
		pptr->v=0;
	}else {
		pptr->k=x;
		pptr->v=y+1;
	}
	return pptr;
}



int count_trays(int* shelf, int m, int x, int y) {
	pair* pptr;
	while (inbound(m,x,y) && (shelf[x]&bits[y])) {
		pptr = nextcoords(m,x,y);
		x=pptr->k;
		y=pptr->v;
		free(pptr);
	}
	if (!inbound(m,x,y)) {
		return 1;
	}
	int ans=0;
	int i;
	shelf[x]|=bits[y];
	int xnext,ynext,dx,dy;
	pptr=nextcoords(m,x,y);
	xnext=pptr->k;
	ynext=pptr->v;
	free(pptr);
	//printf("%d %d %d %d \n",x,y,xnext,ynext);
	//exit(1);
	ans+=count_trays(shelf,m,xnext,ynext);
	for (i=0;i<2;i++) {
		dx=mdir[i][0];
		dy=mdir[i][1];
		if (!inbound(m,x+dx,y+dy)) {
			continue;
		}
		if (!(shelf[x+dx]&bits[y+dy])) {
			shelf[x+dx]|=bits[y+dy];
			ans+=count_trays(shelf,m,xnext,ynext);
			shelf[x+dx]^=bits[y+dy];
		}
	}
	shelf[x]^=bits[y];

	return ans;
}



int main(int argc, char const *argv[])
{
	int i;
	int m,n;
	float x,y;
	int shelf[3]={0};


	bits[0]=1;
	for (i=1;i<25;i++) {
		bits[i]=bits[i-1]<<1;
	}

	scanf("%d %d",&m,&n);
	if (n) {
		for(i=0;i<n;i++) {
			scanf("%f %f",&y,&x);
			//printf("%f %f\n", x,y);
			shelf[(int)x]|=bits[(int)y];
		}
	}

	printf("%d\n",count_trays(shelf,m,0,0));

	return 0;
}




