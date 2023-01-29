import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int city_cnt = Integer.parseInt(br.readLine());
		
		long city_distn[] = new long[city_cnt-1];
		long oil_cost[] = new long[city_cnt];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i=0; i<city_cnt-1; i++) {
			city_distn[i] = Long.parseLong(st.nextToken());
		}
		
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<city_cnt; i++) {
			oil_cost[i] = Long.parseLong(st.nextToken());
		}
		
		long total = city_distn[0] * oil_cost[0];
		long min_cost = oil_cost[0];
		
		for(int i=1; i<city_cnt-1; i++) {
			if(min_cost > oil_cost[i]) {
				min_cost = oil_cost[i];
			}
			
			if(min_cost <= oil_cost[i]) {
				total += min_cost * city_distn[i];
			}
		}
		System.out.print((int)total);
	}
}