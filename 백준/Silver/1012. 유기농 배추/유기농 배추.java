import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
	static boolean visited[][];
	static int arr[][];
	static int need_worm;
	static int size_x;
	static int size_y;
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int t = Integer.parseInt(br.readLine());
		
		for(int i=0; i<t; i++) {
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			size_x = Integer.parseInt(st.nextToken());
			size_y = Integer.parseInt(st.nextToken());
			int cabbage_cnt = Integer.parseInt(st.nextToken());
			
			arr = new int[size_y+1][size_x+1]; 
			visited = new boolean[size_y+1][size_x+1];
			need_worm = 0;
			
			for(int j=0; j<cabbage_cnt; j++) {
				st = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				arr[y][x] = 1;
			}
			
			for(int y=0; y<size_y; y++) {
				for(int x=0; x<size_x; x++) {
					if(arr[y][x] == 1 && !visited[y][x]) {
						need_worm ++;
						dfs(y,x);
					}
				}
			}
	
			sb.append(need_worm + "\n");
		} // t
		
		System.out.print(sb);	
	}
	
	public static void dfs(int y, int x) {
		
		if(arr[y][x] == 1 && !visited[y][x]) {
			visited[y][x] = true;
			
			int up = y-1;
			int down = y+1;
			int left = x-1;
			int right = x+1;
			
			if(up>=0) { dfs(up, x); }
			if(down<=size_y) { dfs(down, x);  }
			if(left>=0) { dfs(y, left); }
			if(right<=size_x) { dfs(y, right); }
			
		}
	} // dfs
	
}