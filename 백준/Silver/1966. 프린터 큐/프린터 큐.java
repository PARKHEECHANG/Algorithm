import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int test_case = Integer.parseInt(br.readLine());

        for(int i=0; i<test_case; i++) { // 테스트 케이스

            Queue<Document> printer = new LinkedList<Document>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken()); // 문서의 개수는 n개
            int m = Integer.parseInt(st.nextToken()); // 궁금한 문서는 m번

            st = new StringTokenizer(br.readLine());
            for(int j=0; j<n; j++) {
                int priority = Integer.parseInt(st.nextToken());
                printer.add(new Document(j, priority)); // ★_★
            }

            int cnt = 1; // 몇 번째로 인쇄될까?

            while(!printer.isEmpty()) {
                Document doc = printer.poll();
                boolean isImportant = true;

                Iterator it = printer.iterator();
                while(it.hasNext()) { // 프린터 탐색
                    Document next_doc = (Document)it.next();
                    if(doc.priority < next_doc.priority) {  // 다음 문서 중요도가 크면
                       isImportant = false; // 현재문서 중요하지않음.
                       break; // 탐색 종료
                    }
                }

                if(isImportant == false) { // 중요하지 않으면
                    printer.add(doc); // 뒤로 보내기
                } else if (isImportant == true) { // 중요하면서
                    if(doc.doc_num==m) { // 내가 찾던 문서 번호라면
                        sb.append(cnt+"\n"); // 출력
                    } else { // 인쇄(poll)는 이미 되었으니 카운트만 해주자
                        cnt++;
                    }
                }
            }

        } // test_case
        System.out.println(sb);
    } // main
}

class Document {
    int doc_num;
    int priority;

    public Document(int doc_num, int priority) {
        this.doc_num = doc_num;
        this.priority = priority;
    }
}
