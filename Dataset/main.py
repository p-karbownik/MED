from HashtagDataSet import TweetsHashtagsDS
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--tag', type=str, default="kaczynski")

args = parser.parse_args()


def main():
    ds = TweetsHashtagsDS(args.tag)
    ds.get_tweets()
    ds.save_df()


if __name__ == '__main__':
    main()
