import java.io.*;

public class 다트게임 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        int case_num = Integer.parseInt(br.readLine());
        for (int c = 1; c <= case_num; c++) {
            int throw_cnt = Integer.parseInt(br.readLine());
            int total = 0;
            for (int i = 0; i < throw_cnt; i++) {
                String[] pos = br.readLine().split(" ");
                int x = Integer.parseInt(pos[0]);
                int y = Integer.parseInt(pos[1]);
                double radius = Math.sqrt(Math.pow(x,2) + Math.pow(y,2));
                
                long distance = (long)Math.ceil(radius);
                 
                if(0<=distance&&distance<=20)
                    distance = 20;
                else if(20<distance&&distance<=40)
                    distance = 40;
                else if(40<distance&&distance<=60)
                    distance = 60;
                else if(60<distance&&distance<=80)
                    distance = 80;
                else if(80<distance&&distance<=100)
                    distance = 100;
                else if(100<distance&&distance<=120)
                    distance = 120;
                else if(120<distance&&distance<=140)
                    distance = 140;
                else if(140<distance&&distance<=160)
                    distance = 160;
                else if(160<distance&&distance<=180)
                    distance = 180;
                else if(180<distance&&distance<=200)
                    distance = 200;
                else
                    distance = 220;
                long p = (220-distance)/20;
                total+=p;
            }
            sb.append("#"+c+" "+total+"\n");
        }
        System.out.print(sb);
    }
}