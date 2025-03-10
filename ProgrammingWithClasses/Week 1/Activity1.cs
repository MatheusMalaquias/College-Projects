using System;

namespace game
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Writeline("Hello World!");
            Console.Writeline("This is in C#.");

            Console.Writeline("What is your favorite color? ");
            string color = Console.ReadLine("");
            Console.Writeline($"Your color is {color}");
        }
    }
}using System;

namespace game
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Writeline("What is your first name? ");
            string first_name = Console.ReadLine("");
            Console.Writeline("What is your last name? ");
            string last_name = Console.ReadLine("");
            Console.Writeline($"Your name is {last_name}, {first_name} {last_name}");
        }
    }
}