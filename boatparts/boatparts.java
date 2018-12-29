

import java.util.*;



public class boatparts {
	
	static Set<String> parts = new HashSet<>();

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int p = sc.nextInt(), n = sc.nextInt();
		sc.nextLine();

		boolean flag = false;
		for (int i=0;i<n;i++) {
			parts.add(sc.nextLine().trim());
			if(!flag&& parts.size()==p) {
				flag = true;
				System.out.println(i+1);
			}
		}

		if(!flag) {
			System.out.println("paradox avoided");
		}
	}
}



