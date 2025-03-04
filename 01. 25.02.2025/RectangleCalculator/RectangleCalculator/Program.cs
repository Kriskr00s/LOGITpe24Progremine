namespace RectangleCalculator
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Ristküliku kalkulaator!");

            Console.WriteLine("Enter first value");
            string firstNumber = Console.ReadLine();
            float floatFirst = float.Parse(firstNumber);

            //tehke sama teise numbriga
            Console.WriteLine("Enter second value");
            string secondNumber = Console.ReadLine();
            float floatSecond = float.Parse(secondNumber);

            //teha pindala ja ümbermõõdu kalkulatsioon
            //teha ruudu, kolmnurga ja ringi pindala ja ümbermõõdu
        }
    }
}
