from readDataset import read_data_set
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, default="../Dataset/test.csv")

args = parser.parse_args()


def main():
    ds = read_data_set(args.path)


if __name__ == '__main__':
    main()
