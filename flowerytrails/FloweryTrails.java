
// Accepted :)

import java.util.*;
import java.io.*;



class Vertex {
	int index;
	Integer dist;
	Set<Integer> parents;

	public Vertex(int i) {
		index = i;
		parents = new HashSet<Integer>();
		dist = null;
	}
}


class Edge {
	Vertex u,v;
	int wt, count;

	public Edge(Vertex u,Vertex v,int wt) {
		this.u = u;
		this.v = v;
		this.wt=wt;
		count = 1;
	}

	public Vertex other(Vertex w) {
		return w.index == u.index? v: u;
	}

	public int other(int w) {
		return w == u.index? v.index: u.index;
	}
}




public class FloweryTrails {
	
	static int p = -1;
	static Vertex [] V;
	static List<Map<Integer,Edge>> L = new ArrayList<>();
	static List<Edge> E = new ArrayList<>();

	public static void addEdge(int a, int b, int wt) {
		// TODO
		if (a==b) {
			// self loops are useless
			return;
		}
		Vertex va = V[a], vb = V[b];
		if (!L.get(a).containsKey(b)) {
			Edge e = new Edge(va,vb,wt);
			L.get(a).put(b, e);
			L.get(b).put(a, e);
			E.add(e);
			return;
		}

		Edge ab = L.get(a).get(b);
		if (ab.wt==wt) {
			ab.count++;
		}else if (ab.wt>wt){
			Edge e = new Edge(va,vb,wt);
			L.get(a).put(b,e);
			L.get(b).put(a,e);
			E.add(e);
		}
	}

	public static void init() {
		V = new Vertex[p];
		for (int i =0;i<p;i++) {
			V[i] = new Vertex(i);
			L.add(new HashMap<Integer,Edge>());
		}

	}

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] tokens = br.readLine().split("\\s+");
		p= Integer.parseInt(tokens[0]);
		int t = Integer.parseInt(tokens[1]);

		init();

		while (t-->0) {
			tokens = br.readLine().split("\\s+");
			int a = Integer.parseInt(tokens[0]);
			int b = Integer.parseInt(tokens[1]);
			int wt = Integer.parseInt(tokens[2]);
			addEdge(a,b,wt);
		}

		spalg(0);

		System.out.println(sumtree(p-1)*2);

	}

	public static void spalg(int src) {
		V[src].dist =0;
		Set<Integer> unvis = new HashSet<>();

		PriorityQueue<Integer> pq = new PriorityQueue<>(p, 
			new Comparator<Integer>() {
				public int compare(Integer a, Integer b) {
					if (V[a].dist==V[b].dist) {
						return 0;
					}
					if (V[a].dist==null) {
						return 1;
					}
					if (V[b].dist==null) {
						return -1;
					}
					return V[a].dist-V[b].dist;
				}
			}
		);

		for (int i =0;i<p;i++) {
			unvis.add(i);
			pq.add(i);
		}
		while (!unvis.isEmpty()) {
			int v = findV(unvis,pq);
			//System.out.println(cand);
			unvis.remove(v);
			// pq.remove(cand);
			if (V[v].dist == null) {
				break;
			}
			for (int u: L.get(v).keySet()) {
					Edge uv = L.get(u).get(v);
					if (!unvis.contains(u)) {
						continue;
					}
					if (V[u].dist==null || V[u].dist> V[v].dist+uv.wt) {
						pq.remove(u);
						V[u].dist = V[v].dist+uv.wt;
						V[u].parents.clear();
						V[u].parents.add(v);
						pq.add(u); // add again as u's priority has changed
					}else if (V[u].dist== V[v].dist+uv.wt) {
						V[u].parents.add(v);
					}
			}
		}
	}

	public static int findV(Set<Integer> unvis, PriorityQueue<Integer> pq) {
		/*int mv = -1;
		Integer md = null;
		for (int v: unvis) {
			if (md==null || (V[v].dist!=null && V[v].dist<md)) {
				mv = v;
				md = V[v].dist;
			}
		}
		return mv;*/
		int mv = pq.poll();
		while(!unvis.contains(mv)) {
			mv = pq.poll();
		}
		return mv;
	}

	public static int sumtree(int dest) {
		//BFS
		boolean[] vis = new boolean[p];
		vis[dest] = true;
		Queue<Integer> q = new LinkedList<>();
		q.add(dest);
		int sm =0;
		while (!q.isEmpty()) {
			int x = q.poll();
			for(int par: V[x].parents) {
				Edge e = L.get(x).get(par);
				sm += e.wt*e.count;
				if (!vis[par]) {
					q.add(par);
					vis[par] = true;
				}
			}
		}
		return sm;
	}
}




