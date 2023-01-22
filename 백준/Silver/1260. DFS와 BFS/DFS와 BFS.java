import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
	static ArrayList<Integer>[] arr;
	static boolean visited[];
	static int[] answer_dfs;
	static int[] answer_bfs;
	static LinkedList<Integer> queue;
	static int index;
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		int node_cnt = Integer.parseInt(st.nextToken());
		int line = Integer.parseInt(st.nextToken());
		int start = Integer.parseInt(st.nextToken());
		
		arr = new ArrayList[node_cnt+1];
		visited = new boolean[node_cnt+1];
		answer_dfs = new int[node_cnt+1];
		answer_bfs = new int[node_cnt+1];
		
		for(int i=1; i<=node_cnt; i++) {
			arr[i] = new ArrayList<>();
		}
		
		for(int i=1; i<=line; i++) {
			st = new StringTokenizer(br.readLine());
			int node_a = Integer.parseInt(st.nextToken());
			int node_b = Integer.parseInt(st.nextToken());
			// 양방향
			arr[node_a].add(node_b);
			arr[node_b].add(node_a);
		}
		
		// 오름차순
		for(int i=1; i<=node_cnt; i++) {
			Collections.sort(arr[i]);
		}
		
		// dfs 준비
		index = 1;
		answer_dfs[index] = start;
		visited[start] = true;
		dfs(start);
		
		// bfs 준비
		index = 0;
		visited = new boolean[node_cnt+1];
		queue = new LinkedList();
		queue.add(start);
		visited[start] = true;
		bfs(start);
		
		while(!queue.isEmpty()) { // 큐에 들어갔다 나오는 요소를 다시 bfs탐색
			int save_poll = queue.poll();
			answer_bfs[++index] = save_poll;
			bfs(save_poll);
		}
		
		// 출력
		for(int i=1; i<=node_cnt; i++) {
			if(answer_dfs[i]!=0) {
				sb.append(answer_dfs[i]+" ");
			}
		}
		
		sb.append("\n");
		
		for(int i=1; i<=node_cnt; i++) {
			if(answer_bfs[i]!=0) {
				sb.append(answer_bfs[i]+" ");
			}
		}
		
		System.out.print(sb);
	} // main
	
	public static void dfs(int current) {
		for(int neighbor : arr[current]) {
			if(visited[neighbor] == false) {
				visited[neighbor] = true;
				answer_dfs[++index] = neighbor;
				dfs(neighbor);
			}
		}
	}
	
	public static void bfs(int current) {
		for(int neighbor : arr[current]) {
			if(visited[neighbor] == false) {
				visited[neighbor] = true;
				queue.add(neighbor); // 방문 노드 큐에 넣기
			}
		}
	}
	
}