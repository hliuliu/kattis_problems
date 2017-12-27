
// Accepted
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
	List<List<Integer> > edges;
	int[] match,victim;

	public BipGraph(int n) {
		this.n=n;
		edges = new ArrayList<>(n+1);
		edges.add(null);
		for (int i=1;i<=n;i++) {
			edges.add( new LinkedList<Integer>());
		}
		match = new int[n+1];
		victim =new int[n+1];
	}

	public void addEdge(int u, int v) {
		edges.get(u).add(v);
		edges.get(v).add(u);
	}

	public boolean matching() {
		int count =0;
		boolean [] visited = new boolean[n+1];
		for (int i=1;i<=n;i++) {
			Arrays.fill(visited, false);
			if (matching(i,visited)) count ++;
		}
		return count ==n;
	}

	private boolean matching(int i, boolean[] visited) {
		for (Integer j: edges.get(i)) {
			if (!visited[j]) {
				visited[j] = true;
				if (victim[j]==0 || matching(victim[j], visited)) {
					match[i] = j;
					victim[j] = i;
					return true;
				}
			}
		}
		return false;
	}

}


