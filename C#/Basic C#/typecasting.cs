using System; 

namespace Basic_Program{
    
  public class Program{
        
    public static void Main(string[] args){
      // Type Casting = Converting a value to a different data type.
      //                Useful when we accept user input (string)
      //                and we want to use it as a number (int, double) 
      //                or we want to convert it to a different data type.
      // Implicit Casting = Automatically done by the compiler.
      // Explicit Casting = Manually done by the programmer.

      double a = 3.14;
      int b = (int)a; // Explicit Casting.
      // int b = Convert.ToInt32(a); // Implicit Casting.
      int c = 123;
      double d = Convert.ToDouble(c) + 0.1;
      int e = 321;
      
      String f = Convert.ToString(e);
      String g = "$";
      char h = Convert.ToChar(g);

      String i = "true";
      bool j = Convert.ToBoolean(i);
      
      Console.WriteLine(b);
      Console.WriteLine(b.GetType()); // To check the type of the variable.
      Console.WriteLine(d);
      Console.WriteLine(d.GetType());
      Console.WriteLine(f);
      Console.WriteLine(f.GetType());
      Console.WriteLine(h);
      Console.WriteLine(h.GetType());
      Console.WriteLine(j);
      Console.WriteLine(j.GetType());
      
      Console.ReadKey();    
    }
  }
}
