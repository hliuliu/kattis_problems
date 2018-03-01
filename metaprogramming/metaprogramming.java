

import java.util.*;
import java.io.*;


public class metaprogramming {
	
	static Map<String,Integer> ENV = new HashMap<>();


	public static boolean evaluate(String var1, String op, String var2) {
		int n1 = ENV.get(var1), n2 = ENV.get(var2);
		switch(op.charAt(0)) {
			case '<':
				return n1<n2;
			case '>':
				return n1>n2;
		}
		return n1==n2;
	}

	public static void process(String line) {
		String [] tokens = line.split("\\s+");
		if (tokens[0].equals("define")) {
			ENV.put(tokens[2], Integer.parseInt(tokens[1]));
		}else {
			String var1 = tokens[1], op = tokens[2], var2 = tokens[3];
			if (ENV.containsKey(var1) && ENV.containsKey(var2)) {
				System.out.println(evaluate(var1,op,var2));
			}else {
				System.out.println("undefined");
			}
		}
	}

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = br.readLine();
		while (line!=null && line.length()>0) {
			process(line);
			line=br.readLine();
		}
	}
}



