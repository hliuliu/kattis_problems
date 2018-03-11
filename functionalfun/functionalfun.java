
//Accepted :)

import java.util.*;
import java.io.*;



public class functionalfun {

	static Map<String,Set<String>> func = new HashMap<>(), preim = new HashMap<>();
	static String line;


	public static boolean getLine(BufferedReader br) throws IOException{
		line = br.readLine();
		return line!=null && line.length()>0;
	}


	public static String test() {
		for(Set<String> sets: func.values()) {
			if (sets.size()>1) {
				return "not a function";
			}
		}

		boolean inj=true,suj=true;

		for(Set<String> sets: preim.values()) {
			if (sets.size()>1) {
				inj = false;
			}
			if (sets.isEmpty()) {
				suj = false;
			}
		}

		return inj&&suj? "bijective": inj? "injective": suj? "surjective": "neither injective nor surjective";
	}

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		while (getLine(br)) {
			boolean first = true;
			for (String dom: line.split("\\s+")) {
				if (!first) {
					func.put(dom, new HashSet<String>());
				}
				first = false;
			}
			first = true;
			getLine(br);
			for(String codom: line.split("\\s+")) {
				if (!first) {
					preim.put(codom, new HashSet<String>());
				}
				first = false;
			}


			getLine(br);
			int n = Integer.parseInt(line);
			while (n-->0) {
				getLine(br);
				String [] corr = line.split("\\s+\\->\\s+");
				preim.get(corr[1]).add(corr[0]);
				func.get(corr[0]).add(corr[1]);
			}


			System.out.println(test());
			func.clear();
			preim.clear();
		}

	}
}











