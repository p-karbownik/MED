from readDataset import read_data_set
from declat import DECLATRunner
from declat import decode_result
from bit_declat import BitDECLATRunner
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, default="../dataset/test.csv")

args = parser.parse_args()


def main():
    ds = read_data_set(args.path)
    dr = DECLATRunner()
    bdr = BitDECLATRunner(ds, 6)
    bdr.run()
    # decode_result(dr.run(ds, 6), len(ds.transactions))


if __name__ == '__main__':
    main()
