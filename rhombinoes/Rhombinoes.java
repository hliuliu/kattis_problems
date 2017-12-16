
// TLE :(
import java.util.*;

public class Rhombinoes {
	static int width =0, height = 0;
	static boolean [][] grid = null, visited = null;
	static ArrayList<ArrayList<LinkedList<BPair>>> nbrs = null;

	static class BPair {
		int x, y;
		public BPair() {
			this(0,0);
		}
		public BPair(int x,int y) {
			this.x=x;
			this.y=y;
		}
	}

	public static void populate(int x, int y) {
		LinkedList<BPair> nlist = nbrs.get(x).get(y);
		if (x>0) {
			nlist.add(new BPair(x-1,y));
		}
		if (x<width-1) {
			nlist.add(new BPair(x+1,y));
		}
		if (((x+y)&1)==1) {
			if (y<height-1) {
				nlist.add(new BPair(x,y+1));
			}
		}else {
			if (y>0) {
				nlist.add(new BPair(x,y-1));
			}
		}
	}

	public static void populateNbrs() {
		nbrs = new ArrayList<ArrayList<LinkedList<BPair>>>(width);
		for (int i=0;i<width;i++) {
			nbrs.add(new ArrayList<LinkedList<BPair>>(height));
			for (int j=0; j<height; j++) {
				nbrs.get(i).add(new LinkedList<BPair>());
				populate(i,j);
			}
		}
	}

	public static boolean gennext(BPair curr) {
		if (curr.y<height-1) {
			curr.y++;
			return true;
		}
		if (curr.x<width-1) {
			curr.x++;
			curr.y=0;
			return true;
		}
		return false;
	}

	public static int dfs(BPair curr) {
		boolean flag = true;
		while (flag && (grid[curr.x][curr.y] || visited[curr.x][curr.y])) {
			flag = gennext(curr);
		}
		if (!flag) {
			return 0;
		}
		LinkedList<BPair> nlist = nbrs.get(curr.x).get(curr.y);
		visited[curr.x][curr.y] = true;
		BPair currNext = new BPair(curr.x,curr.y);
		int ans = 0;
		flag = gennext(currNext);
		for (BPair pair: nlist) {
			if (!grid[pair.x][pair.y] && !visited[pair.x][pair.y]) {
				visited[pair.x][pair.y] = true;
				if (!flag) {
					ans = max(ans,1);
				}else {
					ans = max(ans, dfs(currNext)+1);
				}
				visited[pair.x][pair.y] = false;
			}
		}
		visited[curr.x][curr.y]=false;
		if (flag) {
			ans = max(ans,dfs(currNext));
		}
		return ans;
	}

	public static int max(int a,int b) {return a>b?a:b;}


	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		width = scan.nextInt();
		height = scan.nextInt();
		grid = new boolean[width][height];
		visited = new boolean[width][height];
		int k = scan.nextInt();
		for(int i=0;i<k;i++) {
			grid[scan.nextInt()][scan.nextInt()] = true;
		}
		populateNbrs();
		System.out.println(dfs(new BPair(0,0)));
	}
	
}

