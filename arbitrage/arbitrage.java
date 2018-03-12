

import java.util.*;
import java.io.*;

// Accepted :)

class Edge {
	int u,v;
	double wt;
	int comp;
	Edge(int u, int v, double wt) {
		this.u = u;
		this.v = v;
		this.wt= wt;
		comp = -1;
	}
}


class UF {
	int[] parent;

	public UF(int n) {
		parent = new int[n];
		for (int i =0;i<n;i++) {
			parent[i]=-1;
		}
	}


	public int find(int u) {
		while(parent[u]>=0 && parent[parent[u]]>=0) {
			parent[u] = parent[parent[u]];
			u =parent[u];
		}
		return parent[u]>=0? parent[u]: u;
	}

	public void union(int u, int v) {
		int pu = find(u), pv = find(v);
		if (pu==pv) {
			return;
		}
		/*if (pu>pv) {
			int temp = pu;
			pu=pv;
			pv = temp;
		}*/
		parent[pu]+=parent[pv];
		parent[pv] =pu;
	}

	public int size(int u) {
		return -parent[find(u)];
	}


}


public class arbitrage {
	
	static Map<String,Integer> currencyIndex = new HashMap<>();
	// static Map<Integer,List<Edge>> comps =new HashMap<>();
	static List<Edge> edges = new LinkedList<>();

	static UF uf;


	public static boolean relax(Edge e, double[]dist) {
		if (dist[e.v]>dist[e.u]+e.wt) {
			dist[e.v] =dist[e.u]+e.wt;
			return true;
		}
		return false;
	}

	public static boolean BF(int c) {
		Set<Integer> unvis =new HashSet<>();
		for(int i =0;i<c;i++) {
			unvis.add(i);
		}
		while (!unvis.isEmpty()) {
			int v = -1;
			for (int x_: unvis) {v=x_;break;}
			unvis.remove(v);
			double [] dist = new double[c];
			for (int i=0;i<c;i++) {
				dist[i] = Double.POSITIVE_INFINITY;
			}
			dist[v] = 0;
			int k =uf.size(v);
			for (int i =1;i<k;i++) {
				for (Edge e:edges) {
					if (relax(e,dist)) {
						unvis.remove(e.v);
					}
				}
			}
			for (Edge e: edges) {
				if (relax(e,dist)) {
					return false;
				}
			}
		}
		return true;
	}

	public static boolean readGraph(BufferedReader br) throws IOException {
		int c = Integer.parseInt(br.readLine());
		if (c==0) {
			return false;
		}
		String []currency = br.readLine().split("\\s+");
		for (int i=0;i<c;i++) {
			currencyIndex.put(currency[i], i);
		}
		int r = Integer.parseInt(br.readLine());

		while (r-->0) {
			String[] tokens = br.readLine().split("\\s+|:");
			edges.add(new Edge(currencyIndex.get(tokens[0]),
								currencyIndex.get(tokens[1]),
								Math.log(Double.parseDouble(tokens[2])/Double.parseDouble(tokens[3]))
								));
		}

		uf = new UF(c);

		for (Edge e:edges) {
			uf.union(e.u,e.v);
		}

		System.out.println(BF(c)? "Ok": "Arbitrage");

		currencyIndex.clear();
		edges.clear();

		return true;
	}


	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while (readGraph(br)) {}
		br.close();
	}
}





