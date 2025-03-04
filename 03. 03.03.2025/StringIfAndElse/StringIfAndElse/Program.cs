namespace StringIfAndElse
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
            //peab saama sisestada nime
            //if ja else kontrollib, kas on nimi või on tühi
            //kui leiate kuskilt teksti värviliseks teha, siis kasutage

            string name = Console.ReadLine();

            if (name != "")
            {
                Console.WriteLine("Sisestasid nime: " + name);
            }
            else
            {
                Console.WriteLine("Ei sisestanud nime");
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("ERROR");
                Console.Beep();
                Console.Beep();
                Console.Beep();
                Console.Beep();
                Console.Beep();
                Console.Beep();
                Console.Beep();
            }
        }
    }
}
