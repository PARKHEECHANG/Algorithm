import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());

        Deque deque = new LinkedList();

        for(int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            if(command.equals("push_front")) {
                deque.addFirst(Integer.parseInt(st.nextToken()));
            } else if(command.equals("push_back")) {
                deque.addLast(Integer.parseInt(st.nextToken()));
            } else if(command.equals("pop_front")) {
                sb.append(deque.isEmpty() ? "-1" : deque.pollFirst());
                sb.append("\n");
            } else if(command.equals("pop_back")) {
                sb.append(deque.isEmpty() ? "-1" : deque.pollLast());
                sb.append("\n");
            } else if (command.equals("size")) {
                sb.append(deque.size());
                sb.append("\n");
            } else if(command.equals("empty")) {
                sb.append(deque.isEmpty() ? "1" : "0");
                sb.append("\n");
            } else if(command.equals("front")) {
                sb.append(deque.isEmpty() ? "-1" : deque.peekFirst());
                sb.append("\n");
            } else if(command.equals("back")) {
                sb.append(deque.isEmpty() ? "-1" : deque.peekLast());
                sb.append("\n");
            }

        } // for
        System.out.println(sb);
    } // main
}