import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        Queue<Integer> q = new LinkedList<>();

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int cnt = 1;

        for(int i=1; i<=n; i++) {
            q.add(i);
        }

        sb.append("<");
        while(!q.isEmpty()) {
            if(cnt<k) {
                q.add(q.poll());
                cnt++;
            } else if(cnt==k) { // k번째 사람
                if (q.size() == 1) {
                    sb.append(q.poll()); // 마지막 요소는 ', ' 제거
                } else {
                    sb.append(q.poll()).append(", ");
                }
                cnt = 1;
            }

        }
        sb.append(">");
        System.out.println(sb);

    } // main
}