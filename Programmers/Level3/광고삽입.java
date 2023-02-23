//2021 KAKAO BLIND RECRUITMENT
//https://school.programmers.co.kr/learn/courses/30/lessons/72414

import java.util.*;

class 광고삽입 {
    public int numByTime(String time){
        int hour = Integer.parseInt(time.substring(0, 2));
        int mins = Integer.parseInt(time.substring(3, 5));
        int sec = Integer.parseInt(time.substring(6, 8));
        return hour*3600 + mins*60 + sec;
    }
    
    public String timeByNum(int num){
        int hour = num / 3600;
        num %= 3600;
        int mins = num / 60;
        num %= 60;
        int sec = num;
        return String.format("%02d:%02d:%02d", hour, mins, sec);
    }
    
    public String solution(String play_time, String adv_time, String[] logs) {
        int playTime = numByTime(play_time);
        int advTime = numByTime(adv_time);
        
        long[] viewTable = new long[playTime];
        
        for (int i=0; i<logs.length; i++){
            String[] log = logs[i].split("-");
            int startLogTime = numByTime(log[0]);
            int endLogTime = numByTime(log[1]);
            for (int j=startLogTime; j<endLogTime; j++){
                viewTable[j] += 1;
            }
        }
        
        long currentView = 0;
        int currentAdvTime = 0;
        
        for (int i=0; i<advTime; i++){
            currentView += viewTable[i];
        }
        
        long maxView = currentView;
        
        for (int i=1; i<playTime-advTime+1; i++){
            currentView -= viewTable[i-1];
            currentView += viewTable[i+advTime-1];
            
            if (currentView > maxView){
                currentAdvTime = i;
                maxView = currentView;
            }
        }
        
        return timeByNum(currentAdvTime);
    }
}