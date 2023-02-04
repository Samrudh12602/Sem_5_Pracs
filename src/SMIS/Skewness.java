package SMIS;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Skewness {
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
        float skew= (3*(mean(data)-median(data))/std(data));
        System.out.println("The Mean is: "+mean(data));
        System.out.println("The Median is: "+median(data));
        System.out.println("The Std Deviation is: "+std(data));
        System.out.println("The Skewness is: "+skew);
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
    public static float std(ArrayList dataset)
    {
        Collections.sort(dataset);
        double sum = 0.0, standardDeviation = 0.0;
        int length = dataset.size();

        for(Object num : dataset) {
            sum += (int)num;
        }

        double mean = sum/length;

        for(Object num: dataset) {
            standardDeviation += Math.pow((int)num - mean, 2);
        }
        return (float) Math.sqrt(standardDeviation/length);
    }
}
