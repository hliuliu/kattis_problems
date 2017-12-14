

import java.util.*;


public class Mailbox {

	public static int max(int a,int b) {return a>b?a:b;}
	public static int min(int a,int b) {return a<b?a:b;}

	public static void main(String[] args) {
		Scanner scan =new Scanner(System.in);
		int numcases=scan.nextInt();
		int k=0,m=0;
		int[][][]table;
		for (int i=0;i<numcases;i++) {
			k=scan.nextInt();
			m=scan.nextInt();
			table=new int[k+1][m+1][m+1];
			initTable(table);
			System.out.println( optimalSolution(k,m,table));;
		}
	}
	public static void initTable(int[][][]table) {
		for (int i=0;i<table.length;i++) {
			for (int j=0;j<table[i].length;j++) {
				for (int k=0;k<table[i][j].length;k++) {
					table[i][j][k]=-1;
				}
			}
		}
	}


	public static int optimalSolution(int k, int m, int[][][]table) {
		return func(k,1,m,table);
	}

	public static int func(int k, int i, int j, int[][][]table) {
		if (i>j) {
			return 0;
		}
		if (table[k][i][j]>=0) {
			return table[k][i][j];
		}
		if (k ==1) {
			table[k][i][j]=j*(j+1)/2-i*(i-1)/2;
			return table[k][i][j];
		}
		int minval=Integer.MAX_VALUE;
		for (int s=i;s<=j;s++) {
			minval=min(minval,s+max(func(k-1,i,s-1,table),func(k,s+1,j,table)));
		}
		table[k][i][j]=minval;
		return minval;
	}

}



