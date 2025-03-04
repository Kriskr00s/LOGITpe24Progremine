namespace DataTypes
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Data types!");

            //täisnumber
            int bigNumber = 1234567890;
            Console.WriteLine(bigNumber);

            //komaga number ??
            double comaNumber = 12.5;
            Console.WriteLine(comaNumber);

            //tähemärk
            string stringVar = "asd456$%^&*(     84u5098lnfigu+-";
            Console.WriteLine(stringVar);

            float floatVariable = 123.123f;
            Console.WriteLine(floatVariable);

            char charVariable = '2';
            Console.WriteLine(charVariable);

            bool boolVariable = false;
            Console.WriteLine(boolVariable);
        }
    }
}
