using System; 

namespace Basic_Program{
    
  public class Program{
        
    public static void Main(string[] args){
      
      Console.WriteLine("Whats your name?");
      String name = Console.ReadLine();
      
      Console.WriteLine("Whats your age?");
      int age = Convert.ToInt32(Console.ReadLine());
    
      Console.WriteLine("Hello " + name);
      Console.WriteLine("You are " + age + " years old");

  
      Console.ReadKey();
    }
  }
}
