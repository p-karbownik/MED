from HashtagDataSet import TweetsHashtagsDS
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--tag', type=str, default="kaczynski")
parser.add_argument('--number', type=int, default=10000)

args = parser.parse_args()


def main():
    ds = TweetsHashtagsDS(args.tag)
    ds.get_tweets(args.number)
    ds.save_df()


if __name__ == '__main__':
    main()
