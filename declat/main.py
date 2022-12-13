from readDataset import read_data_set
from declat import DECLATRunner
from declat import decode_result
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, default="../Dataset/test.csv")

args = parser.parse_args()


def main():
    ds = read_data_set(args.path)
    dr = DECLATRunner()
    decode_result(dr.run(ds, 6), len(ds.transactions))


if __name__ == '__main__':
    main()
