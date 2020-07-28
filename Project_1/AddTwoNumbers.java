public class AddTwoNumbers {

  public static void change(int x){
    x = 5;
  }

   public static void main(String[] args) {
      int num1 = 5, num2 = 15, sum;
      change(num2);
      sum = num1 + num2;

      System.out.println("Sum of these numbers: "+sum);
   }
}
