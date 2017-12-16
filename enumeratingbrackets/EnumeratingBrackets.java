
import java.math.*;
import java.util.*;

public class EnumeratingBrackets {

	public static long[] catalan = new long[1001];
	public static char[] pref = new char[2000];
	public static int prefLength = 0;
	public static final long MAXVAL = (long)Math.pow(10,18);

	public static void initCatalan() {
		catalan[0] = 1;
		for (int i=1; i<catalan.length;i++) {
			catalan[i]= catalan[i-1]*2*(2*i-1)/(i+1);
			if (catalan[i]>MAXVAL) {
				catalan[i]=MAXVAL;
			}
		}
	}

	// public static void removeRange(int start,int end) {
	// 	for (int i=end-1;i>=start;i--) {
	// 		pref.remove(i);
	// 	}
	// }

	public static void nextp(int n) {
		int used = prefLength/2;
		if (used>1) {
			if (pref[prefLength-3]=='(') {
				char last = pref[prefLength-1];
				pref[prefLength-3]= last;
				prefLength-=2;
			}else {
				int i = prefLength-3;
				while (pref[i]!='(') {i--;}
				pref[i] = ')';
				pref[i+1]='(';
			}
		}else if (used ==1) {
			prefLength = 0;
		}
		else {
			prefLength = n*2;
			for (int i=0;i<n;i++) {
				pref[i]='(';
				pref[n+i]=')';
			}
		}
	}

	public static String joinStr() {
		char [] res = new char[prefLength];
		int i=0;
		for(char c: pref) {
			if(i==prefLength) {
				break;
			}
			res[i++]=(char)c;
		}
		return new String(res);
	}

	public static String gen(int n,long m) {
		if (n==0) {
			return "";
		}
		if (n==1) {
			return "()";
		}
		long counter = 0;
		int used =0;
		prefLength = 0;
		// System.out.println(joinStr());
		while (m>counter) {
			nextp(n);
			used = prefLength/2;
			counter += (catalan[n-used]);
			// System.out.println(joinStr());
		}
		counter-=catalan[n-used];
		m-=(counter);
		String curr = joinStr();
		String rec = gen(n-used,m);
		return curr+rec;
	} 
	
	public static void main(String[] args) {
		initCatalan();
		// System.out.println(Arrays.toString(catalan));
		// System.out.println(catalan[5]);
		// System.out.println(MAXVAL);
		Scanner scan = new Scanner (System.in);
		int n = scan.nextInt();
		long m = scan.nextLong();
		System.out.println(gen(n/2,m));
	}
}




