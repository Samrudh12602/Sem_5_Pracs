package TOC;
import java.util.Scanner;
public class FiniteAutomata {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        int i=0;
        System.out.println("Enter the DFA in 5 tuple format ");
        System.out.println("Number of states :");
        int states= sc.nextInt();
        System.out.println("Number of inputs: ");
        int inputs=sc.nextInt();
        int[] alpha=new int[inputs];
        int[] st= new int[states];
        for (int j=0;j<states;j++){
            st[j]=j;
        }
        for (int j=0;j<inputs;j++){
            alpha[j]=j;
        }
        System.out.print("states are ");
        for (int j=0;j<states;j++){
            System.out.print("q"+st[j]+" ");
        }
        System.out.println();
        System.out.print("input alphabets are ");
        for (int j=0;j<inputs;j++){
            System.out.print(alpha[j]+" ");
        }
        System.out.println();
        int[][] trans=new int[states][inputs];
        System.out.println("Enter the Transition Table: ");
        for(int j=0;j<states;j++){
            for(int k=0;k<inputs;k++){
                System.out.print("\nenter the transition state of q"+st[j]+" X "+alpha[k]+" : ");
                trans[j][k]=sc.nextInt();
            }
        }
        System.out.println("transition table : ");
        for(int j=0;j<states;j++){
            for(int k=0;k<inputs;k++){
                System.out.print(" ( q"+st[j]+" ");
                System.out.print("X "+alpha[k]+" ) ");
                System.out.print("= q"+trans[j][k]+" , ");
            }
            System.out.println();
        }
        System.out.print("choose one initial state from : ");
        for(int j=0;j<states;j++)
        {
            System.out.print(" q"+st[j]+" ");
        }
        System.out.println();
        int istate=sc.nextInt();
        System.out.println("so u chose initial state as : q"+istate);
        System.out.println("enter number of final states");
        int nf= sc.nextInt();
        System.out.println();
        System.out.println("choose final state from : ");
        for(int j=0;j<states;j++)
        {
            System.out.print(" q"+st[j]+" ");
        }
        System.out.println();
        int[] fstate=new int[nf];
        for(int j =0;j<nf;j++){
            fstate[j]=sc.nextInt();
        }
        System.out.println();
        System.out.print("so u chose the following as your final states :");
        for(int j =0;j<nf;j++){
            System.out.print(" q"+fstate[j]+" ");
        }
        System.out.println();
        int choice;
        do {
            System.out.println("enter a string to check : ");
            String w=sc.next();
            int cursor=istate;
            if(w.startsWith("e")){
                for(int j=0; j <nf;j++){
                    if((fstate[j]==istate)){
                        System.out.println("valid string");
                        i++;
                    }
                }
            }else{
                char[] ch = new char[w.length()];
                for (int j = 0; j <w.length(); j++) {
                    ch[j] = w.charAt(j);
                }
                System.out.print("q"+cursor);
                for(int j=0;j<w.length();j++){
                    cursor=trans[cursor][Integer.parseInt(String.valueOf(ch[j]))];
                    System.out.print("--> q"+cursor);
                }
                System.out.println();
                for(int j=0;j<fstate.length;j++)
                {
                    if(cursor==fstate[j]){
                        System.out.println("valid string ");
                        i++;
                    }
                }
            }
            if(i==0)
                System.out.println("not valid");
            System.out.println("the string ended at q"+cursor+" state");
            System.out.println("press 1 to do it again ,0 to exit");
            choice= sc.nextByte();
            i=0;
        } while(choice!=0);
    }
}
