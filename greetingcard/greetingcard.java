import java.util.*;
import java.io.*;

public class greetingcard{
	public static void main(String [] args)
	{
		BufferedReader scanner = new BufferedReader(new InputStreamReader(System.in));

		long results = 0;
		String[] coordinates = new String[2];
		try{
			int numCoors = Integer.parseInt(scanner.readLine());
			int[][] listCoors = new int[numCoors][2];
			for(int i = 0; i < numCoors; i++){
				coordinates = scanner.readLine().split(" ");

				listCoors[i][0] = Integer.parseInt(coordinates[0]);
				listCoors[i][1] = Integer.parseInt(coordinates[1]);
			}
			System.out.println(process(listCoors));
			// for(int i = 0; i < numCoors; i++){
			// 	for(int j = i+1; j < numCoors; j++){
			// 		if(listCoors[i][0] == listCoors[j][0]){
			// 			if(Math.abs(listCoors[i][1] - listCoors[j][1]) == 2018){
			// 				results++;
			// 			}
			// 		}
			// 		else if(Math.abs(listCoors[i][0] - listCoors[j][0]) == 1118){
			// 			if(Math.abs(listCoors[i][1] - listCoors[j][1]) == 1680){
			// 				results++;
			// 			}
			// 		}
			// 		else if(Math.abs(listCoors[i][0] - listCoors[j][0]) == 1680){
			// 			if(Math.abs(listCoors[i][1] - listCoors[j][1]) == 1118){
			// 				results++;
			// 			}
			// 		}
			// 		else if(Math.abs(listCoors[i][0] - listCoors[j][0]) == 2018){
			// 			if(listCoors[i][1] == listCoors[j][1]){
			// 				results++;
			// 			}
			// 		}
			// 	}
			// }
			// System.out.println(results);
		}
		catch (IOException e){
		}
	}


	static int[][] combs = {{2018,0},{0,2018},{1118,1680},{1680,1118}, {-2018,0}, {0,-2018}, {-1118,1680}, {1118,-1680},{-1118,-1680},
	{1680,-1118},{-1680,1118},{-1680,-1118}};

	public static Pair[] nbrs(Pair p) {
		Pair[] pair  = new Pair [combs.length];
		int i=0;
		for (int [] comb:combs) {
			pair[i]=new Pair (p.x+comb[0],p.y+comb[1]);
			i++;
		}
		return pair;
	}


	public static boolean inset(Pair p, Set <Pair> pts) {
		for (Pair pp:pts) {
			if (p.equals(pp)) {
				return true;
			}
		}
		return false;
	}


	public static int process(int[][]listCoors) {
		Set <Pair> pts  = new HashSet<Pair>();
		int count = 0;
		for (int[] coor: listCoors) {
			Pair p = new Pair(coor[0],coor[1]);
			// System.out.println(pts);
			for (Pair np: nbrs(p)) {
				// System.out.println(np);
				if (inset(np,pts)) {
					// System.out.println("yes");
					count ++;
				}
			}
			pts.add(p);
		}
		return count;
	}


	// public static int process(int[][]listCoors) {
		// HashMap <Integer, LinkedList<Pair>> xvals, yvals;
		// xvals = new HashMap<Integer, LinkedList<Pair>>();
		// // yvals = new HashMap<Integer, LinkedList<Pair>>();
		// for (int[] coor : listCoors) {
		// 	Pair p = new Pair(coor[0],coor[1]);
		//
		// 	if (!xvals.containsKey(p.x)) {
		// 		xvals.put(p.x,new LinkedList<Pair>());
		// 	}
		//
		// 	xvals.get(p.x).add(p);
		// 	// yvals.put(p.y, p);
		// }
		//
		// // System.out.println(xvals);
		//
		// int count = 0;
		//
		// for (Integer xval: xvals.keySet()) {
		// 	for (int[]comb:combs) {
		// 		if (!xvals.containsKey(xval+comb[0])) {
		// 			continue;
		// 		}
		//
		// 		for (Pair first: xvals.get(xval)) {
		// 			for (Pair snd: xvals.get(xval+comb[0])) {
		// 				if (comb[0]==0 && first.y-snd.y==comb[1]) {
		// 					count++;
		// 				}
		// 				else if (comb[0]>0 && Math.abs(first.y-snd.y)== comb[1]) {
		// 					// System.out.println(first);
		// 					// System.out.println(snd);
		// 					count++;
		// 				}
		// 			}
		// 		}
		//
		// 	}
		// }
		//
		//
		//
		// return count;
	// }



}


class Pair {
	int x,y;
	public Pair() {
		this(0,0);
	}

	public Pair(int a, int b) {
		x=a;y=b;
	}

	public String toString() {
		return String.format("(%d,%d)",x,y);
	}

	public boolean equals(Object other) {
		Pair op = (Pair) other;
		return op.x==x && op.y==y;
	}
}
