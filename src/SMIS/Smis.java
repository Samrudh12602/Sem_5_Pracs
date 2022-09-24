//Write a Program to calculate Mean Median and Mode of the given Individual dataset.

package SMIS;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
public class Smis {
    public static void main(String[] args) {
        ArrayList<Integer> data ;
        Scanner s = new Scanner(System.in) ;
        int n;
        System.out.println("Enter the Length of Dataset:");
        n=s.nextInt();
        data= new ArrayList<>(n );
        System.out.println("Enter the Dataset:");
        for(int i=0;i<n;i++)
        {
            data.add(s.nextInt());
        }
        System.out.println("The Mean is: "+mean(data));
        System.out.println("The Median is: "+median(data));
        System.out.println("The Mode is: "+mode(data));
    }
    public static float mean(ArrayList dataset){
        float average;
        int sum=0;
        for(int i=0;i<dataset.size();i++){
            sum+=(int)dataset.get(i);
        }
        average=(float)sum/dataset.size();
        Collections.sort(dataset);
        System.out.println(dataset);
        return average;
    }
    public static float median(ArrayList dataset){
        Collections.sort(dataset);
        if (dataset.size() % 2 != 0)
            return (int) dataset.get( (dataset.size() / 2));
        return (float) ((float)  ((int)dataset.get((dataset.size() - 1) / 2) + (int)dataset.get(dataset.size() / 2)) / 2.0);
    }
    public static int mode(ArrayList dataset){
        Collections.sort(dataset);
        int maxcount=0,mode=0;
        for(int i=0;i<dataset.size();i++){
            int count=0;
            for(int j=0;j<dataset.size();j++){
                if((int)dataset.get(j)==(int)dataset.get(i)){
                    count++;
                }
                if(count>maxcount){
                    maxcount=count;
                    mode=(int)dataset.get(i);
                }
            }
        }
        return mode;
    }
}
