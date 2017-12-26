
import java.util.*;


public class paintball {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		BipGraph G = new BipGraph(n);
		for (int i =0; i<m;i++) {
			G.addEdge(sc.nextInt(),sc.nextInt());
		}
		if (G.matching()) {
			boolean first = true;
			for (int target: G.match) {
				if (!first) {
					System.out.println(target);
				}
				first = false;
			}
		}else {
			System.out.println("Impossible");
		}
	}
}





class BipGraph {
	int n;
	List<Set<Integer> > edges;
	boolean[] visited;
	int[] match;

	public BipGraph(int n) {
		this.n=n;
		edges = new ArrayList<>(n+1);
		edges.add(null);
		for (int i=1;i<=n;i++) {
			edges.add( new HashSet<Integer>());
		}
		visited = new boolean[n+1];
		match = new int[n+1];
	}

	public void addEdge(int u, int v) {
		edges.get(u).add(v);
		edges.get(v).add(u);
	}

	public boolean matching() {
		return matching(1);
	}

	private boolean matching(int start) {
		if (start>n) {
			return true;
		}
		for (Integer other: edges.get(start)) {
			if(match[other]==0) {
				match[other] = start;
				if (matching(start+1)) {
					return true;
				}
				match[other] = 0;
			}
		}
		return false;
	}

}


