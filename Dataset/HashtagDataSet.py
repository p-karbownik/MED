import snscrape.modules.twitter as sntwitter
import pandas as pd
from unidecode import unidecode


class TweetsHashtagsDS:

    def __init__(self, hash_tag):
        self._df = None
        self.hash_tag = hash_tag

    def get_tweets(self, max_tweets) -> None:
        separators = [",", ".", "\\", ";", "|", "'", "?", ")", "!", "-", ":"]
        tweets_tags_list = []

        last_inserted_index = 0
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'#{self.hash_tag}').get_items()):
            if i > max_tweets:
                break
            if i % 500 == 0:
                print(i)
            content = tweet.content.split()
            hash_tags = [word for word in content if word.startswith("#")]
            hash_tags_list = []
            for tag in hash_tags:
                for sep in separators:
                    if sep in tag:
                        tag = tag.split(sep)
                        tag = tag[0]
                if len(tag) > 1:
                    hash_tags_list.append([last_inserted_index, unidecode(tag.lower())])

            if len(hash_tags_list) > 0:
                tweets_tags_list.extend(hash_tags_list)
                last_inserted_index += 1

        self._df = pd.DataFrame(tweets_tags_list, columns=['tweet_id', 'tag'])

    def save_df(self) -> None:
        if self._df is not None:
            self._df.to_csv(f'{self.hash_tag}.csv', index=False)

    def load_df(self) -> None:
        try:
            self._df = pd.read_csv(f'Dataset/{self.hash_tag}.csv')
        except FileNotFoundError:
            self._df = None
            print("No such a file was found!")

    def get_df(self) -> pd.DataFrame:
        return self._df
