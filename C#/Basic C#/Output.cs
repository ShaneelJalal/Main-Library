using System; 

namespace Basic_Program
{
  public class Program
  {
    public static void Main(string[] args)
    {
      Console.Write("I like pizza"); // No new line
      Console.WriteLine("Its really good!"); // New line

      /* 
      This
      is
      a 
      multi-line
      comment
      */
      Console.Write("\tCODE"); // Tabs/indents the line
      Console.Write("\bCODE"); // Backspaces the line
      Console.Write("\nCODE"); // New line
      Console.Readkey(); // Waits for user input  
    }
  }
}
