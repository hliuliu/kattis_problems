

import java.util.*;
import java.io.*;


public class cd {

  public static int[] getmn(BufferedReader br) throws IOException {
    String [] tokens = br.readLine().split("\\s+");
    return new int[] {Integer.parseInt(tokens[0]),Integer.parseInt(tokens[1]) };
  }

  public static void main(String[] args) throws IOException {
    Scanner sc = new Scanner(System.in);
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int [] vals = getmn(br);
    int n = vals[0];
    int m = vals[1];
    BitSet own = new BitSet(1000000000);

    while (n>0 && m>0) {

      for (int i =0;i<n;i++) {
        own.set(Integer.parseInt(br.readLine()));
      }

      int ct = 0;

      for (int i=0;i<m;i++) {
        if (own.get(Integer.parseInt(br.readLine()))) {
          ct++;
        }
      }
      System.out.println(ct);

      vals = getmn(br);
      n = vals[0];
      m = vals[1];
      own.clear();
    }
  }
}
