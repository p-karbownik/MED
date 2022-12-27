from declat.bit_declat import BitDECLATRunner
from declat.bit_declat import decode
from declat.readDataset import read_data_set
from declat.readBitDataset import read_bit_data_set
from declat.declat import DECLATRunner
from declat.declat import decode_result
from ploting.lattice import LatticePlotter
from ploting.support_chart import ChartPlotter
from ploting.time import draw_time_charts
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--bit_mode', type=bool, default=True)
parser.add_argument('--draw_time_charts_mode', type=bool, default=False)
parser.add_argument('--name', type=str, default="test")
parser.add_argument('--support', type=int, default=3)
parser.add_argument('--show_results', type=bool, default=False)
parser.add_argument('--lattice', type=bool, default=False)
parser.add_argument('--supp_chart', type=bool, default=True)

args = parser.parse_args()


def main():
    if not args.draw_time_charts_mode:
        if args.bit_mode:
            ds = read_bit_data_set(f"dataset/{args.name}.csv")
            bdr = BitDECLATRunner(ds, args.support)
            results = decode(bdr.run(), args.show_results)
        else:
            ds = read_data_set(f"dataset/{args.name}.csv")
            dr = DECLATRunner()
            results = decode_result(dr.run(ds, args.support), len(ds.transactions), args.show_results)

        if args.lattice:
            lp = LatticePlotter(results.copy(), args.name, args.support)
            lp.plot_lattice()
        if args.supp_chart:
            cp = ChartPlotter(args.name, results)
            cp.create_chart()
    else:
        draw_time_charts()


if __name__ == '__main__':
    main()
