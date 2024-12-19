using Spectre.Console;
using ScottPlot;
using System.Diagnostics;
namespace ChartsAndGraphs
{
    internal class Program
    {
        static List<int> Series = new List<int>();
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a value");
            int val = int.Parse(Console.ReadLine());
            Alg(val);

            int[] xs = new int[Series.Count];
            for (int i = 0; i < Series.Count; i++)
            {
                xs[i] = i;
            }

            int[] ys = Series.ToArray();
            ScottPlot.Plot myPlot = new();
            myPlot.Add.Scatter(xs, ys);
            myPlot.XLabel("Sequence position");
            myPlot.YLabel("Sequence value");
            myPlot.Title("Colatz conjecture mapping");
            myPlot.SavePng("demo.png", 500, 500);
            string filePath = "\"C:\\Users\\samev\\source\\repos\\Maths\\ChartsAndGraphs\\ChartsAndGraphs\\bin\\Debug\\net8.0\\demo.png\"";
            Process.Start(new ProcessStartInfo(filePath) { UseShellExecute = true });
            Console.WriteLine("Graph plotted");
        }
        static void Alg(int x)
        {
            Series.Add(x);
            //Console.WriteLine(x);
            if (x == 1)
            {
                return;
            }
            else if (x % 2 == 0)
            {
                x = x / 2;
            }
            else { x = 3 * x + 1; };

            Alg(x);
        }
    }
}
