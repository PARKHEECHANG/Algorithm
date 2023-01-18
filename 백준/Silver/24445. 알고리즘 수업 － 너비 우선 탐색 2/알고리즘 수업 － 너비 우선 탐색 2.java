import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	static ArrayList<Integer>[] arr;
	static boolean visited[];
	static int visit_order[];
	static int index;
	static int node_cnt;
	static LinkedList<Integer> queue;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int node_cnt = Integer.parseInt(st.nextToken()); // 노드의 수
		int edge = Integer.parseInt(st.nextToken()); // 간선의 수
		int start = Integer.parseInt(st.nextToken()); // 시작점
		
		visited = new boolean[node_cnt+1]; // 방문 판단
		visit_order = new int[node_cnt+1]; // 방문 순서
		
		// 각 노드별 ArrayList
		arr = new ArrayList[node_cnt+1];
		for(int i=1; i<=node_cnt; i++) { 
			arr[i] = new ArrayList<>();
		}
		
		// 양방향 간선 정보
		for(int i=1; i<=edge; i++) {
			st = new StringTokenizer(br.readLine());
			int node_a = Integer.parseInt(st.nextToken());
			int node_b = Integer.parseInt(st.nextToken());
			arr[node_a].add(node_b);
			arr[node_b].add(node_a);
		}
		
		// 노드 내림차순 정렬
		for(int i=1; i<=node_cnt; i++) {
			Collections.sort(arr[i],Collections.reverseOrder());
		}
		
		queue = new LinkedList(); // 큐 생성
		visited[start] = true; // 시작점 방문
		queue.add(start); // 큐에 시작점 추가
		bfs(start); // 탐색

		while(!queue.isEmpty()) { 
			int q_p = queue.poll(); // POLL == 방문 기준
			visit_order[q_p] = ++index;
			bfs(q_p); // 방문하지 않은 주변 노드 다시 큐에 삽입 
			// 깊이 있는 건 나중에..POLL
		}
		
		// 출력
		for(int i=1; i<=node_cnt; i++) {
			sb.append(visit_order[i]+"\n");
		}
		System.out.print(sb);
	} // main
	
	public static void bfs(int current) {
		for(int neighbor : arr[current]) {
			if(visited[neighbor]!=true) { 
				visited[neighbor] = true;
				queue.add(neighbor); // 주변 노드부터(너비우선)  IN
			}
		}
	} // bfs
	
}