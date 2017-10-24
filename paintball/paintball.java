
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
		// int ct =0;
		for (int i=1;i<=n;i++) {
			if (match[i]==0 && !matching(i)) {
				return false;
			}
		}
		return true;
	}

	private boolean matching(int start) {
		for (Integer other: edges.get(start)) {
			if (!visited[other]) {
				// match[start] = (int)other;
				visited[other] = true;
				if (match[other]==0 || matching(match[other])) {
					match[other] = start;
					return true;
				}
				// visited[other] = false;
				// match[start] = 0;
			}
		}
		return false;
	}

}


