//10059
//연습문제

import java.io.*;

/*
5
0721
2107
0507
0705
1313
*/

public class 유효기간 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        int testcase = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= testcase; tc++) {
            String number = br.readLine().replace(" ", "");
            Integer[] _number = {
                Integer.parseInt(number.substring(0,2)),
                Integer.parseInt(number.substring(2,4))
            };
            String result = "NA";
            if (1 <= _number[0] && _number[0] <= 12){
                result = "MMYY";
            }
            if (1 <= _number[1] && _number[1] <= 12){
                if (result == "NA"){
                    result = "YYMM";
                } else {
                    result = "AMBIGUOUS";
                }
            }
            sb.append("#"+tc+" "+result+"\n");
        }
        System.out.print(sb);
    }
}