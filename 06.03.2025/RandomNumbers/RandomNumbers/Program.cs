namespace RandomNumbers
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
            //nüüd tuleb kasutada switchi, et näidata numbrist 1-st 6-ni

            int number = new Random().Next(1, 7);

            switch (number)
            {
                case 1:
                    Console.WriteLine("veeretasid nr " + number);
                    break;

                case 2:
                    Console.WriteLine("veeretasid nr " + number);
                    break;

                case 3:
                    Console.WriteLine("veeretasid nr " + number);
                    break;

                case 4:
                    Console.WriteLine("veeretasid nr " + number);
                    break;

                case 5:
                    Console.WriteLine("veeretasid nr " + number);
                    break;

                case 6:
                    Console.WriteLine("veeretasid nr " + number);
                    break;



                default:
                    Console.WriteLine("Error");
                    break;
            }
            {
                

            }



            }
        }
    }
