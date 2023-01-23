import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
	static boolean visited[][];
	static int arr[][];
	static LinkedList<Integer> house_cnt_list;
	static int complex_cnt;
	static int house_cnt;
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		house_cnt_list = new LinkedList<Integer>(); // 주택 수 리스트
	
		// 입력
		int n = Integer.parseInt(br.readLine()); // 범위
		arr = new int[n+1][n+1];
		visited	= new boolean[n+1][n+1];
		for(int i=0; i<n; i++) {
			String line = br.readLine();
			for(int j=0; j<n; j++) {
				arr[i][j] = (int)(line.charAt(j))-48;
			}
		}
		
		for(int y=0; y<n; y++) {
			for(int x=0; x<n; x++) {
				if(arr[y][x] == 1 && !visited[y][x]) {
					complex_cnt ++;
					dfs(y, x, n);
					int tmp = house_cnt;
					house_cnt_list.add(tmp);
					house_cnt = 0;
				}
			}
		}
		
		// 출력
		// 집의 수를 오름차순으로 정렬
		Collections.sort(house_cnt_list);
		sb.append(complex_cnt + "\n");
		while(!house_cnt_list.isEmpty()) {
			sb.append(house_cnt_list.poll() + "\n");
		}	
		System.out.print(sb);
	} // main
	
	public static void dfs(int y, int x, int n) {
		
		if(arr[y][x] == 1 && !visited[y][x]) {
			visited[y][x] = true;
			house_cnt++;
			
			int up = y-1;
			int down = y+1;
			int left = x-1;
			int right = x+1;
			
			if(up>=0) { dfs(up, x, n); }
			if(down<=n) {dfs(down, x, n); }
			if(left>=0) {dfs(y, left, n); }
			if(right<=n) {dfs(y, right, n); }
			
		}
	} // dfs
		
}