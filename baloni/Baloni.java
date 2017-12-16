

import java.util.*;

public class Baloni {

	static class Node {
		int value;
		Node next;

		public Node(int val) {
			value=val;
			next=null;
		}
		
	}

	public static Node LL(int[]list) {
		Node head,curr;
		head=new Node(0);
		curr=head;
		for (int v : list) {
			curr.next=new Node(v);
			curr=curr.next;
		}
		return head.next;
	}

	public static void main(String[] args) {
		Scanner inp = new Scanner(System.in);
		int n= inp.nextInt();
		int[]ballons = new int[n];
		for(int  i=0;i<n;i++) {
			ballons[i]=inp.nextInt();
		}
		Node head=LL(ballons);
		int count=0;
		while(head!=null) {
			Node curr=head;
			Node back=null;
			int ht=head.value;
			while(curr!=null) {
				if(ht==curr.value) {
					ht--;
					if(curr==head) {
						head=head.next;
					}else {
						back.next=curr.next;
					}
				}else {
					back=curr;
				}
				curr=curr.next;

			}
			count+=1;
		}
		System.out.println(count);
	}
	
}


