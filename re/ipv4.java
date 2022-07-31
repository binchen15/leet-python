import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Scanner;

class Solution{

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        while(in.hasNext()){
            String IP = in.next();
            System.out.println(IP.matches(new MyRegex().pattern));
        }

    }
}

//Write your code here

class MyRegex {
    static String p = "([0-9]{1,2}|[01][0-9]{2}|2[0-4][0-9]|25[0-5])";
    static String pattern = String.join(".", p, p, p, p);
    static {
        // System.out.println(pattern);
    }
}
