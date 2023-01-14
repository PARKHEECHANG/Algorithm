import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()); // 큐 사이즈
        int m = Integer.parseInt(st.nextToken()); // 뽑아낼 수의 개수

        // 큐 생성
        Deque deque = new LinkedList();
        for (int i = 1; i <= n; i++) {
            deque.add(i);
        }

        // 찾는 수
        int find[] = new int[m];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            find[i] = Integer.parseInt(st.nextToken());
        }

        // 찾기
        int cnt = 0; // 2, 3번 연산의 횟수
        for (int i = 0; i < m; i++) { // find[i] 부터 찾기

            while (true) {
                int peek_first = (int) deque.peekFirst();
                int peek_last = (int) deque.peekLast();

                // find[i]의 위치 찾기
                Iterator it = deque.iterator();
                int find_location = 1;
                while(it.hasNext()) {
                    int next_num = (int)it.next();
                    if(next_num == find[i]) {
                        break;
                    }
                    find_location++;
                }

                if (peek_first == find[i]) { //  내가 찾는 숫자면
                    deque.poll(); // 1번 연산
                    break;
                } else if (find_location-1 <= deque.size()-find_location ) { // 앞쪽이 가까우면
                    deque.addLast(deque.pollFirst()); // 2번 연산
                    cnt++;
                } else if (find_location-1 > deque.size()-find_location ) { // 뒤쪽이 가까우면
                    deque.addFirst(deque.pollLast()); // 3번 연산
                    cnt++;
                }
            }
        }
        System.out.println(cnt);
    } // main
}
