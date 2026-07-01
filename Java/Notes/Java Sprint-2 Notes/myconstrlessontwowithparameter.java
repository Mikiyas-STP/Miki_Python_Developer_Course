public class myconstrlessontwowithparameter {
  int x;

  public myconstrlessontwowithparameter(int y) {
    x = y;
  }

  public static void main(String[] args) {
   myconstrlessontwowithparameter myObj = new myconstrlessontwowithparameter(5);
    System.out.println(myObj.x);
  }
}

// Outputs 5