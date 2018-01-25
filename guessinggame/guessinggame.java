
import java.util.*;

public class guessinggame {
	

	public static boolean check(List<Integer> lows, List<Integer> highs, int target) {
		for (int i: lows) {
			if (i>=target) {
				return false;
			}
		}
		for (int i: highs) {
			if (i<=target) {
				return false;
			}
		}
		return true;
	}

	public static boolean play(Scanner sc) {
		List<Integer> lows = new LinkedList<>(), highs = new LinkedList<>();
		int target = -1;
		while (true) {
			target = sc.nextInt();
			if (target==0) {return false;}
			sc.next();
			String resp = sc.next();
			if (resp.equals("low")) {
				lows.add(target);
			}else if (resp.equals("high")) {
				highs.add(target);
			}else {
				System.out.println(
					check(lows,highs,target)? "Stan may be honest": "Stan is dishonest"
				);
				return true;
			}
		}
	}


	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (play(sc)) {}
	}

}


