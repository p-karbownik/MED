import argparse

from bit_declat import BitDECLATRunner, decode
from declat import DECLATRunner
from declat import decode_result
from readDataset import read_data_set

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, default="../dataset/test.csv")

args = parser.parse_args()


def main():
    ds = read_data_set(args.path)
    dr = DECLATRunner()
    decode_result(dr.run(ds, 6), len(ds.transactions), True)
    print("------------------------------------------------")
    bdr = BitDECLATRunner(ds, 6)
    decode(bdr.run(), len(ds.transactions), True)


if __name__ == '__main__':
    main()
