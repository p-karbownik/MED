import snscrape.modules.twitter as sntwitter
import pandas as pd


class TweetsHashtagsDS:

    def __init__(self, hash_tag):
        self._df = None
        self.hash_tag = hash_tag

    def get_tweets(self, max_tweets=10000) -> None:
        separators = [",", ".", "\\", ";", "|", "'", "?", ")", "!", "-", ":"]
        tweets_tags_list = []

        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'#{self.hash_tag}').get_items()):
            if i > max_tweets:
                break
            content = tweet.content.split()
            hash_tags = [word for word in content if word.startswith("#")]
            for tag in hash_tags:
                for sep in separators:
                    if sep in tag:
                        tag = tag.split(sep)
                        tag = tag[0]
                if len(tag) > 1:
                    tweets_tags_list.append([i, tag])

        self._df = pd.DataFrame(tweets_tags_list, columns=['tweet_id', 'tag'])

    def save_df(self) -> None:
        if self._df is not None:
            self._df.to_csv(f'{self.hash_tag}.csv', index=False)

    def load_df(self) -> None:
        self._df = pd.read_csv(f'Dataset/{self.hash_tag}.csv')

    def get_df(self) -> pd.DataFrame:
        return self._df
