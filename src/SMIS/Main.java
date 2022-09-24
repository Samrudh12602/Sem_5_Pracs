package SMIS;
//Write a Program to calculate Mean Median and Mode of the given Individual dataset.
public class Main {
    public static void main(String[] args) {
        int data[];
    }
    public static float mean(int dataset[]){
        float average;
        int sum=0;
        for(int i=0;i<dataset.length;i++){
            sum+=dataset[i];
        }
        average=sum/dataset.length;
        return average;
    }
}
