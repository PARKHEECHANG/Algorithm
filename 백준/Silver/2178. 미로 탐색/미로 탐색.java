import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	static int y_size, x_size;
	static int arr[][], visited[][];
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		StringTokenizer st = new StringTokenizer(br.readLine());
		y_size = Integer.parseInt(st.nextToken());
		x_size = Integer.parseInt(st.nextToken());
		arr = new int[y_size][x_size];
		visited = new int[y_size][x_size];

		for(int y=0; y<y_size; y++) {
			String line = br.readLine();
			for(int x=0; x<x_size; x++) {
			arr[y][x] = Integer.parseInt(line.charAt(x)+"");
			}
		}
		
		bfs(0,0);
		
		System.out.print(arr[y_size-1][x_size-1]);
		
	} // main
	
	public static void bfs(int y, int x) {
		int[] move_x = {-1,1,0,0};
		int[] move_y = {0,0,-1,1};
		int cur_x, cur_y;
		
		Queue<Integer> q = new LinkedList<Integer>();
		q.offer(x);
		q.offer(y);
		visited[y][x] = 1;
		
		while(!q.isEmpty()) {
			x = q.poll();
			y = q.poll();
			for(int i=0; i<4; i++) {
				cur_x = x + move_x[i];
				cur_y = y + move_y[i];
				if(cur_x>=0 && cur_y>=0 && cur_x<x_size && cur_y<y_size) {
					if(arr[cur_y][cur_x] == 1 && visited[cur_y][cur_x] == 0) {
						visited[cur_y][cur_x] = 1;
						arr[cur_y][cur_x] = arr[y][x] + 1;
						q.offer(cur_x);
						q.offer(cur_y);
					}
				}
			}
		}
		
	} // bfs
	
}