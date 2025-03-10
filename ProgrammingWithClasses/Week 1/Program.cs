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
}