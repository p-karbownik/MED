from declat.readDataset import read_data_set
from declat.declat import DECLATRunner
from declat.declat import decode_result
from ploting.lattice import LatticePlotter
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, default="ksiazki")
parser.add_argument('--support', type=int, default=6)
parser.add_argument('--lattice', type=bool, default=True)

args = parser.parse_args()


def main():
    ds = read_data_set(f"Dataset/{args.name}.csv")
    dr = DECLATRunner()
    results = decode_result(dr.run(ds, args.support), len(ds.transactions))
    if args.lattice:
        lp = LatticePlotter(results, args.name)
        lp.plot_lattice()


if __name__ == '__main__':
    main()
