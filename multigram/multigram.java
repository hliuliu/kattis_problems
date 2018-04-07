

import java.util.*;

public class multigram {
	
	static String word = null;

	public static int ctoi(char c) {
		return (int)(c) - (int)('a');
	}

	public static boolean isAnagram(String s1,String s2) {
		if (s1.length()!=s2.length()) {
			return false;
		}
		int [] tally = new int[26];
		for (char c: s1.toCharArray()) {
			tally[ctoi(c)]++;
		}
		for (char c: s2.toCharArray()) {
			int i = ctoi(c);
			if (tally[i]<=0) {
				return false;
			}
			tally[i]--;
		}
		// by pigeonhole principle, tally is all 0's at this point
		return true;
	}

	public static void test() {
		for (int d =1;d<word.length();d++) {
			if (word.length()%d==0) {
				boolean flag = false;
				for (int i=d;i<word.length();i+=d) {
					if (!isAnagram(word.substring(0,d),word.substring(i,i+d))) {
						flag = true;
						break;
					}
				}
				if (!flag) {
					System.out.println(word.substring(0,d));
					return;
				}
			}
		}
		System.out.println(-1);
	}

	public static void main(String[] args) {
		word = new Scanner(System.in).next();
		test();
	}
}


