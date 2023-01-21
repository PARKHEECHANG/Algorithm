import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine()); // 테스트 케이스
		
		for(int i=0; i<t; i++) {
			StringBuilder sb = new StringBuilder();
			Deque<String> deque = new ArrayDeque();
			String command = br.readLine(); // 함수
			int arr_length = Integer.parseInt(br.readLine()); // 배열 길이
			String str = br.readLine(); // 배열
			
			str = str.substring(1, str.length()-1); // 대괄호 제거
			String arr[] = new String[arr_length];
			arr = str.split(","); // ',' 분리하여 배열에 넣기
			
			for(int j=0; j<arr.length; j++) { // 배열 덱에 넣기
				deque.add(arr[j]);
			}
			
			boolean use_r = false;
			int d_cnt = 0; 
			
			for(int j=0; j<command.length(); j++) {
				if(command.charAt(j)=='R' && use_r == false) { // R커맨드로 꺼내는 방향 정하기
					use_r = true;
				} else if(command.charAt(j)=='R' && use_r == true) {
					use_r = false;
				} else if(command.charAt(j)=='D' && use_r == false) { // 정방향이면
					d_cnt ++;
					deque.pollFirst(); // 처음 숫자 꺼내기
				} else if(command.charAt(j)=='D' && use_r == true) { // 역방향이면
					d_cnt ++;
					deque.pollLast(); // 마지막 숫자 꺼내기
				}
			}
			
			if(d_cnt <= arr_length) { // D커맨드가 배열 길이를 넘으면 안됌
				String result[] = new String[arr_length-d_cnt];
				
				if(use_r==true) { // 역방향이면
					for(int j=0; j<result.length; j++) {
						result[j] = deque.pollLast(); // 뒤에서부터 저장
					}
				} else if(use_r==false) { // 정방향이면
					for(int j=0; j<result.length; j++) {
						result[j] = deque.pollFirst(); // 앞에서부터 저장
					}
				}
				
				sb.append("[");
				for(int j=0; j<result.length; j++) {
					sb.append(result[j]);
					sb.append(",");
				}
				
				if(sb.length()>2) { // 마지막 콤마 제거
					sb.deleteCharAt(sb.length()-1);
				}
				
				sb.append("]\n");
	
			} else if(d_cnt > arr_length) { // D커맨드가 입력한 배열크기를 넘으면
				sb.append("error\n"); // error발생
			}
			
			System.out.print(sb);
		} // t

	} // main
}
