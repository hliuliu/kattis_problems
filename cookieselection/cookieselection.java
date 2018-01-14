
import java.util.*;

public class cookieselection {
	static PriorityQueue<Integer> lt, gt;


	public static void adjust() {
		while (lt.size()>gt.size()) {
			gt.add(lt.poll());
		}
		while (gt.size()-lt.size()>1) {
			lt.add(gt.poll());
		}
	}

	public static int median() {
		adjust();
		int ret = gt.poll();
		adjust();
		return ret;
	}

	public static void insert(int value) {
		if (!lt.isEmpty() && value<lt.peek()) {
			lt.add(value);
		}else {
			gt.add(value);
		}
		//adjust();
	}

	public static void main(String[] args) {
		gt = new PriorityQueue<>();
		lt = new PriorityQueue<>(11,
			new Comparator<Integer> () {
				public int compare(Integer a,Integer b) {
					return b-a;
				}
			}
		);

		Scanner sc= new Scanner(System.in);
		while (sc.hasNextLine()) {
			String line = sc.nextLine();
			if (line.charAt(0)=='#') {
				System.out.println(median());
			}else {
				insert(Integer.parseInt(line));
			}
		}
	}
}

