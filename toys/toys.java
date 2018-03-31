

import java.util.*;


public class toys {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt(), k = sc.nextInt();
		int res = 0;
		for (int i =2;i<=t;i++) {
			res = (res+k)%i;
		}
		System.out.println(res);
	}
}



