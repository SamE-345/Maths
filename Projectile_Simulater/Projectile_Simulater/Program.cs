using ScottPlot;
using ScottPlot.Statistics;
using System.Diagnostics;
namespace Projectile_Simulater
{
    internal class Program
    {
        
        static double u = 0;
        static List<double> heights = new List<double>();
        static double a = -9.81;
        static double angle = 0;
        static void Main(string[] args)
        {

            Console.WriteLine("Enter initial velocity");
            u = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("angle");
            angle = Convert.ToDouble(Console.ReadLine());
            double i = 1;
            heights.Add(Height(0));
            while (Height(i) > 0)
            {
                heights.Add(Height(i));
                i+= 0.2;
            }
            double[] xs = new double[heights.Count];
            for (int j = 1; j < heights.Count; j++)
            {
                xs[j] = 0.2*j*u*Math.Cos(angle);
            }

            double[] ys = heights.ToArray();
            ScottPlot.Plot myPlot = new();
            myPlot.Add.Scatter(xs, ys);
            myPlot.SavePng("demo.png", 500, 500);
            
            string filePath = "\"C:\\Users\\samev\\source\\repos\\Maths\\Projectile_Simulater\\Projectile_Simulater\\bin\\Debug\\net8.0\\demo.png\"";
            Process.Start(new ProcessStartInfo(filePath) { UseShellExecute = true });
        }
        static double Height(double time)
        {
            return (u*Math.Sin(angle) * time + 0.5 * a * Math.Pow(time, 2));
        }

    }
}
