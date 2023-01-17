import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;
import java.util.StringTokenizer;


public class Main {
	static ArrayList<Integer>[] arr;
	static boolean[] visited;
	static int[] visit_order;
	static int node_cnt;
	static int index;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		node_cnt = Integer.parseInt(st.nextToken()); // 노드의 수
		int edge = Integer.parseInt(st.nextToken()); // 간선의 수
		int start = Integer.parseInt(st.nextToken()); // 시작점
		
		arr = new ArrayList[node_cnt+1];
		visited = new boolean[node_cnt+1];
		visit_order = new int[node_cnt+1];
		
		for(int i=1; i<=node_cnt; i++) { // 각 노드별 ArrayList
			arr[i] = new ArrayList<>();
		}
		
		for(int i=1; i<=edge; i++) { // 간선 반복
			st = new StringTokenizer(br.readLine());
			int node_1 = Integer.parseInt(st.nextToken());
			int node_2 = Integer.parseInt(st.nextToken());
			// 양방향 간선
			arr[node_1].add(node_2);
			arr[node_2].add(node_1);
		}
		
		// 인접 정점 내림차순 방문
		for(int i=1; i<=node_cnt; i++) {
			Collections.sort(arr[i], Collections.reverseOrder());
		}
		
		visited[start] = true;
		dfs(start);
		
		//출력
		for(int i=1; i<=node_cnt; i++) {
			sb.append(visit_order[i]+"\n");
		}
		
		System.out.println(sb);
	} // main
	
	public static void dfs(int current) {
		visit_order[current] = ++index; // 방문할때마다 ++
		for(int neighbor : arr[current]) {
			if(visited[neighbor]!=true) {
				visited[neighbor] = true;
				dfs(neighbor); 
			}
		}
	} // dfs
    
}