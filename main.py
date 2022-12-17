from declat.readDataset import read_data_set
from declat.declat import DECLATRunner
from declat.declat import decode_result
from ploting.lattice import LatticePlotter
from ploting.support_chart import ChartPlotter
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, default="movies")
parser.add_argument('--support', type=int, default=3)
parser.add_argument('--show_results', type=bool, default=False)
parser.add_argument('--lattice', type=bool, default=True)
parser.add_argument('--supp_chart', type=bool, default=True)

args = parser.parse_args()


def main():
    ds = read_data_set(f"dataset/{args.name}.csv")
    dr = DECLATRunner()
    results = decode_result(dr.run(ds, args.support), len(ds.transactions), args.show_results)
    if args.lattice:
        lp = LatticePlotter(results.copy(), args.name, args.support)
        lp.plot_lattice()
    if args.supp_chart:
        cp = ChartPlotter(args.name, results)
        cp.create_chart()


if __name__ == '__main__':
    main()
