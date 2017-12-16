
import java.util.*;


public class Font {

	public static int[] bits;

	public static void initBits() {
		bits=new int[27];
		bits[0]=1;
		for (int i=1;i<27;i++) {
			bits[i]=bits[i-1]<<1;
		}
	}

	public static int hashWord(String word) {
		//System.out.println(word);
		int m=0;
		for (char c: word.toCharArray()) {
			m|=bits[(int)c-(int)'a'];
		}
		return m;
	}

	public static void main(String[] args) {
		initBits();
		Scanner inp = new Scanner(System.in);
		int n = inp.nextInt();
		inp.nextLine();
		int[] masks = new int [n];
		for(int i=0;i<n;i++) {
			masks[i]=hashWord(inp.nextLine().trim());
		}
		int target = bits[26]-1;
		int[] nb = new int [bits[n]];
		for (int i=0; i<n; i++) {
			nb[bits[i]]=masks[i];
		}
		int count =0;
		for (int i=2;i<bits[n];i++) {
			if (nb[i]==0) {
				int x=i&-i;
				nb[i]=nb[i^x]|nb[x];
			}
			if (nb[i]==target) {
				count++;
			}
		}
		System.out.println(count);
	}
	
}




