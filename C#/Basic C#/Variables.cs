using System; 

namespace Basic_Program
{
    public class Program
    {
        public static void Main(string[] args)
        {
            // Variables
            int x; // Declaration
            x = 123; // Initialization
            int y = 456; // Declaration and Initialization
            int z = x + y; // adding two ints
            int age = 21;
            double height = 1.75; // Double stores decimals
            bool alive = true; // Boolean stores true or false
            char symbol = '@'; // Char stores a single character
            String name = "James"; // String stores a string of characters
            String userName = symbol + name; 

            // Console.WriteLine(x);
            // Console.WriteLine(y);
            // Console.WriteLine(z);
            Console.WriteLine("Hello " + name);
            Console.WriteLine("You are " + age + " years old");
            Console.WriteLine("You are " + height + "m tall");
            Console.WriteLine("Are you alive: " + alive);
            Console.WriteLine("Your symbol is: " + symbol);
            Console.WriteLine("Your username is: " + userName);
            Console.ReadKey(); // Waits for user input  
        }
    }
}
