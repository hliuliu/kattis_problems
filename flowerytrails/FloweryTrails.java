
import java.util.*;
 
public class FloweryTrails {
 
    static class Point {
        int n;
        Set<Trail> trails;
        int dist;
        //Set<Trail> prev;
        Trail[] prev;
        int len;
 
        public Point(int n) {
            this.n = n;
            this.dist = Integer.MAX_VALUE;
            trails = new HashSet<Trail>(2);
            //prev= new HashSet<Trail>(2);
            len=0;
        }
    }
 
    private static class PointComparator implements Comparator<Point> {
        public int compare(Point o1, Point o2) {
            return o1.dist - o2.dist;
        }
    }
 
    static class Trail {
        int l;
        Point p1, p2;
        //boolean isPopular;
 
        public Trail(Point p1, Point p2, int l) {
            this.p1 = p1;
            this.p2 = p2;
            this.l = l;
        }
    }

    static Point other(Trail t, Point p) {return p==t.p1? t.p2 : t.p1;}
 
    /*static void recAdd(Set<Trail> s, Point p) {
    	if (p.prev.isEmpty()) {
    		return;
    	}
    	s.addAll(p.prev);
    	for (Trail t: p.prev) {
    		//System.out.println("in trail");
    		recAdd(s,other(t,p));
    	}
    }
*/
	static void iterAdd(Set<Trail> s, Point p) {
    	Queue<Point> q = new LinkedList<Point>();
    	q.add(p);
    	while (!q.isEmpty()) {
    		p=q.poll();
    		for (int i=0 ; i< p.len;i++) {
    			Trail t=p.prev[i];
    			s.add(t);
    			q.add(other(t,p));
    		}
    	}
    }

    static Set<Trail> hike(PriorityQueue<Point> q, Point goal) {
    	Set<Trail> opt = new HashSet<Trail>();
    	Set<Trail> visited = new HashSet<Trail>();
    	while (!q.isEmpty()) {
    		Point u = q.poll();
    		//System.out.println(u.n);
    		for (Trail t: u.trails) {
    			Point po = other(t,u);
    			/*if (!q.contains(po)) {
    				System.out.println("point not in here");
    				continue;
    			}*/
    			int w = u.dist+t.l;
    			if (w<po.dist) {
    				po.dist=w;
    				po.len=0;
    				//System.out.println("adding points");
    				//System.out.println(u.n+" "+po.n);
    				if (!visited.contains(t)) {
	    				po.prev[po.len++]=t;
	    				q.add(po);
	    			}
	    			visited.add(t);
    			}
    			else if (w==po.dist) {
    				//System.out.println(u.n+" "+po.n);
    				if (!visited.contains(t)) {
	    				po.prev[po.len++]=t;
	    				q.add(po);
	    			}
	    			visited.add(t);
	    		}

    		}
    	}
    	iterAdd(opt,goal);
    	return opt;
    }
 
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
 
        int P = in.nextInt(),
            T = in.nextInt();
 
        Point points[] = new Point[P];
        for (int i = 0; i < P; i++) {
            points[i] = new Point(i);
        }
        points[0].dist = 0;
 
        for (int i = 0; i < T; i++) {
            int one = in.nextInt(),
                two = in.nextInt(),
                l = in.nextInt();
            Point p1 = points[one],
                  p2 = points[two];
            Trail trail = new Trail(p1, p2, l);
            p1.trails.add(trail);
            p2.trails.add(trail);
        }

        for (Point p: points) {
        	p.prev=new Trail[p.trails.size()];
        }
 
        PriorityQueue<Point> q = new PriorityQueue<Point>(P, new PointComparator());
        /*for (Point p: points){
        	q.add(p);
        }*/
        q.add(points[0]);
       
        Set<Trail> sol = hike(q,points[P-1]);

        int sum=0;
        for (Trail t: sol) {
        	sum+=t.l;
        	//System.out.println("Trail "+t.l);
        }

        System.out.println(2*sum);

    }
}