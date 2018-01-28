


import java.util.*;
import java.io.*;

//Weighted Union Find (Accepted)
public class UnionFind
{
  int[] parent,stack;
  
  public UnionFind(int n)
  {
    parent = new int[n];
    stack = new int[n];
    for (int i = 0; i < n; i++)
    {
      parent[i] = -1;
    } 
  }
  
  public boolean connected(int p, int q)
  {
    return (find(p) == find(q));
  }
  
  public int find(int p)
  {
    
    int top = 0;
    
    while(parent[p] >= 0)
    {
      stack[top++] = p;
      p = parent[p];
    }    
    
    // Why did path compression make it worse?
    // while (--top>=0) {
    //   parent[stack[top]] = p;
    // }
    
    return p;    
  }

  public void union(int p, int q)
  {
    p = find(p);
    q = find(q);
    
    if (p == q)
    {
     	return; 
    }
    //p and q parents are not the same so they are not in the same component.
    //Find out which component has the smaller size and set the parent of that
    //component to the root of the larger component.
    else
    {
     	if (parent[p] > parent[q])
      {
        parent[q] += parent[p];		
        parent[p] = q;          
      }  
     	else
      {
       	parent[p] += parent[q];
        parent[q] = p;
      } 
    }  
  }
    
	public static void main (String args[])
    throws IOException
  {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    String input = br.readLine();
    
    String[] splitInput = input.split("\\s+");
    
    UnionFind a = new UnionFind(Integer.parseInt(splitInput[0]));
    
    int numOps = Integer.parseInt(splitInput[1]);
    
    StringBuilder sb = new StringBuilder();
    
    for (int i = 0; i < numOps; i++)
    {
       input = br.readLine();
      
       splitInput = input.split("\\s+");
      
     	 String op = splitInput[0];
      
       if (op.charAt(0) == '?')
       {
         sb.append(a.connected(Integer.parseInt(splitInput[1]),Integer.parseInt(splitInput[2]))? "yes":"no");
         sb.append("\n");
       }
       else if (op.charAt(0) == '=')
       {
         a.union(Integer.parseInt(splitInput[1]),Integer.parseInt(splitInput[2]));
       } 
    }
    
    System.out.println(sb);
  }
}



















