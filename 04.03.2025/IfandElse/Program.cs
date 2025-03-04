namespace IfandElse
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Sisesta enda vanus");

            int vanus = int.Parse(Console.ReadLine());

            if (vanus >= 0 && vanus <= 18)
            {
                Console.WriteLine("Oled alaealine");
            }
           

            else if (vanus >= 18 && vanus < 65)
            {
                Console.WriteLine("Oled täiskasvanu");
            }
            else
            {
                Console.WriteLine("Oled pensionär");
            }
        }
    }
}
