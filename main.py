import argparse
from Dataset.HashtagDataSet import TweetsHashtagsDS

parser = argparse.ArgumentParser()
parser.add_argument('--tag', type=str, default="kaczynski")

args = parser.parse_args()


def main():
    ds = TweetsHashtagsDS(args.tag)
    ds.load_df()
    df = ds.get_df()
    if df is not None:
        print(df.head())


if __name__ == '__main__':
    main()
