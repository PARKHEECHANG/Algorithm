import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int meeting_cnt = Integer.parseInt(br.readLine());
		Meeting meeting[] = new Meeting[meeting_cnt];
		
		for(int i=0; i<meeting_cnt; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			meeting[i] = new Meeting(start, end);
		}
		
		// Comparator 객체 사용
		Comparator<Meeting> comparator = new Comparator<Meeting>(){
			@Override
			public int compare(Meeting a, Meeting b) {
				if(a.end == b.end) {
					return a.start - b.start;
				}
	
				return a.end - b.end;
			}
		};
		
		Arrays.sort(meeting, comparator);
		
		// 람다 함수 사용
//		Arrays.sort(meeting, (a,b) -> a.end - b.end );
		
		int now_end = meeting[0].end;
		int cnt = 1;
		
		for(int i=1; i<meeting_cnt; i++) {
			if(now_end <= meeting[i].start) {
				now_end = meeting[i].end;
				cnt ++;
			}
		}
		
		System.out.print(cnt);
	} // main
			
}

class Meeting {
	int start;
	int end;
	
	public Meeting(int start, int end) {
		this.start = start;
		this.end = end;
	}	
}