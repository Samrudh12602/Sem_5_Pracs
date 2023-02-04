//Write a Program to calculate GM and HM of the given Individual dataset.
package SMIS;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
public class GMHM {
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
        System.out.println("The GM is: "+GM(data));
        System.out.println("The HM is: "+HM(data));

    }
    public static float GM(ArrayList dataset){
        Collections.sort(dataset);
        float gm,sum=0;
        for(int i=0;i<dataset.size();i++){
            sum+=(float)Math.log10(Double.valueOf(dataset.get(i).toString()));
        }
        float value = sum/dataset.size();
        gm=(float) Math.pow(10,value);
        return gm;
    }
    public static float HM(ArrayList dataset){
        Collections.sort(dataset);
        float hm,sum=0;
        for(int i=0;i<dataset.size();i++){
            sum+=(float)(1/Double.valueOf(dataset.get(i).toString()));
        }
        float value = dataset.size()/sum;
        return value;
    }
}
