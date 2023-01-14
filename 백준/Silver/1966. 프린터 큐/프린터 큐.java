import javax.print.Doc;
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
            int orgin_printer[] = new int[n]; // 초기 프린터 상태

            st = new StringTokenizer(br.readLine());
            for(int j=0; j<n; j++) {
                int priority = Integer.parseInt(st.nextToken());
                orgin_printer[j] = priority;
                printer.add(new Document(j, priority));
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
                    if(doc.doc_num==m) { // 문서 번호도 같으면
                        sb.append(cnt+"\n"); // 출력
                    } else {
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

---
## trouble
* 중요도가 같은 문서들이 있으면, 큐가 회전하면서 M번 문서의 위치도 변하여 M번 문서를 찾기 어려움. 
* 키(처음 상태의 문서 위치)와 값(중요도)의 형태가 필요하다고 느낌.
* 큐의 요소들을 반복하여 꺼내는 법을 모름.

따라서 문서 클래스(문서번호, 중요도)를 통해 문서 객체 생성

큐의 내용을 반복하기 위해 Iterator 학습.


## 구조 변경

(중요도 판단, poll, add) **=>** (poll, 중요도 판단, add)


## 이외에도 <int[]> 활용하는 방법
``` java
LinkedList<int[]> q = new LinkedList<>();

for (int i = 0; i < N; i++) {
	q.add(new int[] { i, Integer.parseInt(st.nextToken()) });
}
```

