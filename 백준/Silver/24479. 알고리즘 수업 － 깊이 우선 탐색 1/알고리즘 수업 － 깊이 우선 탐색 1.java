import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;
import java.util.StringTokenizer;


public class Main {
	static ArrayList<Integer>[] arr;
	static boolean[] visited;
	static int[] answer;
	static int node_cnt;
	static int visit_order;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		node_cnt = Integer.parseInt(st.nextToken());
		int edge = Integer.parseInt(st.nextToken());
		int start = Integer.parseInt(st.nextToken());
		arr = new ArrayList[node_cnt+1];
		visited = new boolean[node_cnt+1];
		answer = new int[node_cnt+1];
		
		for(int i=0; i<=node_cnt; i++) { // 노드의 수만큼 arr생성
			arr[i] = new ArrayList<>();
		}
		
		while(edge-->0) { // 간선이 존재하면
			st = new StringTokenizer(br.readLine());
			int node_1 = Integer.parseInt(st.nextToken());
			int node_2 = Integer.parseInt(st.nextToken());
			// 양방향 간선
			arr[node_1].add(node_2);
			arr[node_2].add(node_1);
		}
		
		// 인접 정점은 오름차순으로 방문
		for(int i=1; i<node_cnt; i++) {
			Collections.sort(arr[i]);
		}
		
		visited[start] = true;
		dfs(start);
		
		for(int i=1; i<=node_cnt; i++) {
			sb.append(answer[i]+"\n");
		}
		System.out.print(sb);
	} // main
	
	public static void dfs(int current) {
		answer[current] = ++visit_order; // ++방문 순서
		for(int neighbor : arr[current]) { // arr[] 인접 노드 하나씩 추출
			if(!visited[neighbor]) {
				visited[neighbor] = true;
				dfs(neighbor);
			}
		}
	} // dfs
	
}
