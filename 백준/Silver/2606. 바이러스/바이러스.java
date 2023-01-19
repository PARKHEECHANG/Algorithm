import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static ArrayList<Integer>[] arr;
	static boolean visited[];
	static int visit_cnt;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int com_cnt = Integer.parseInt(br.readLine()); // 컴퓨터의 수
		int line_cnt = Integer.parseInt(br.readLine()); // 연결의 수
	
		arr = new ArrayList[com_cnt+1];
		for(int i=1; i<=com_cnt; i++) {
			arr[i] = new ArrayList(); // 각 컴퓨터[i]마다 ArrayList
		}
		
		for(int i=1; i<=line_cnt; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int com_a = Integer.parseInt(st.nextToken());
			int com_b = Integer.parseInt(st.nextToken());
            // 양방향 감염
			arr[com_a].add(com_b); 
			arr[com_b].add(com_a);
		}
		
		visited = new boolean[com_cnt+1];
		
		int start = 1;
		visited[start] = true;
		infct(start);
		
		// 출력
		System.out.print(visit_cnt);
	
	} // main
	
	public static void infct(int current) {
		for(int next : arr[current]) {
			if(visited[next] == false) {
				visited[next] = true;
				visit_cnt++;
				infct(next);
			}
		}
	} // 감염
	
}

