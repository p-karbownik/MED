from hashtag_data_set import TweetsHashtagsDS


def main():
    topics = ["politics", "movies", "ksiazki", "cinema", "muzyka"]
    numbers = [500, 1000, 2000, 5000, 7500]

    for topic, number in zip(topics, numbers):
        ds = TweetsHashtagsDS(topic, number)
        ds.get_tweets()
        ds.save_df()

    for topic, number in zip(topics, numbers):
        ds = TweetsHashtagsDS(f'#{topic}', number)
        ds.get_tweets()
        ds.save_df()


if __name__ == '__main__':
    main()
