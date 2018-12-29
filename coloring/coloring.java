


import java.util.*;
import java.io.*;



public class coloring {

	static int n=0;
	static List<Set<Integer>> G = new ArrayList<>();

	public static int toInt(String s) {
		return Integer.parseInt(s);
	} 

	public static void readGraph() throws IOException{
		BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
		n = toInt(br.readLine());
		for (int i =0;i<n;i++) {

			Set<Integer> adj =new TreeSet<Integer>();
			for (String nbr: br.readLine().split("\\s+")) {
				adj.add(toInt(nbr));
			}

			G.add(adj);
		}

		br.close();
	}


	public static int minColour(int[] colours, int curr, int ncol) {
		if (curr==n) {
			return ncol;
		}
		int ans = n;
		Set<Integer> legal = new HashSet<>();
		for (int i =0;i<ncol;i++) {
			legal.add(i);
		}
		for (int u: G.get(curr)) {
			if (u>curr) {
				break;
			}
			legal.remove(colours[u]);
		}
		for (int c: legal) {
			colours[curr] = c;
			ans = Math.min(ans, minColour(colours,curr+1,ncol));
		}
		colours[curr] = ncol;
		ans =Math.min(ans, minColour(colours,curr+1,ncol+1));
		return ans;
	}


	public static void main(String[] args) {
		try {
			readGraph();
		}catch (IOException ex) {
			System.exit(1);
		}
		System.out.println(minColour(new int[n], 1, 1));
	}
	
}










