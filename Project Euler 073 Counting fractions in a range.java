import java.io.*;
import java.util.Scanner;

public class Solution {

    private static long rank(int A, int D){
        long[] mylist = new long[D + 1];
        for(int q=0; q<mylist.length; q++){
            mylist[q] = q / A;
        }
        for(int q=1; q<mylist.length; q++){
            for(int r=2*q; r<mylist.length; r+=q){
                mylist[r]-=mylist[q];
            }
        }
        long sum = 0;
        for(long x : mylist){
            sum+=x;
        }
        return sum;
    }
    
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)){
            int A = sc.nextInt();
            int D = sc.nextInt();
            System.out.println(rank(A, D) - rank(A+1, D) - 1);
        }
    }
}
