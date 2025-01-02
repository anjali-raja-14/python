import javax.swing.*;//calender
import java.awt.color.ICC_ColorSpace;
import java.util.*;
public class ain {
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
//        System.out.println("enter a number:");
//        int n =sc.nextInt();
        System.out.println("enter a number 1 or 0:");
       double num =sc.nextDouble();
        if (num==1){
            System.out.println("enter your marks:");
            double marks=sc.nextDouble();


            do{
                System.out.println("this is good");
                 

            }while(marks>=90);

            do{
                System.out.println("this is also good");
            }while(marks<=89 && marks>=59);
            do{
                System.out.println("this is good as well");
            }while(marks<=59 && marks>=0);

        }else {
            System.out.println("nothing is there for uh");
        }


        }




    }









        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.








// import javax.swing.*;//calender
// import java.awt.color.ICC_ColorSpace;
// import java.util.*;
// public class Main {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
// //        System.out.println("enter a number:");
// //        int n =sc.nextInt();
//         System.out.println("enter a number 1 or 0:");
//        double num =sc.nextDouble();
//         if (num==1){
//             System.out.println("enter your marks:");
//             double marks=sc.nextDouble();


//             do{
//                 System.out.println("this is good");
                 

//             }while(marks>=90);

//             do{
//                 System.out.println("this is also good");
//             }while(marks<=89 && marks>=59);
//             do{
//                 System.out.println("this is good as well");
//             }while(marks<=59 && marks>=0);

//         }else {
//             System.out.println("nothing is there for uh");
//         }


//         }




//     }