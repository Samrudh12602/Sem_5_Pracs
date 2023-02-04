package SMIS;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class StdDeviation {
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
        System.out.println("The Mean Deviation is: "+meanDeviation(data));
        System.out.println("The Std Deviation is: "+std(data));
    }
    public static float meanDeviation(ArrayList dataset)
    {
        float absSum = 0;
        for (int i = 0; i < dataset.size(); i++)
            absSum = absSum + Math.abs(Float.valueOf(dataset.get(i).toString())) - mean(dataset);
        return absSum / dataset.size();
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
    public static float mean(ArrayList dataset){
        float average;
        int sum=0;
        for(int i=0;i<dataset.size();i++){
            sum+=(int)dataset.get(i);
        }
        average=(float)sum/dataset.size();
        Collections.sort(dataset);
        return average;
    }
}
