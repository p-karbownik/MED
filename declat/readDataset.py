import pandas as pd


class DataSet:

    def __init__(self, elements: list, transactions: dict):
        self.elements = elements
        self.transactions = transactions


def read_data_set(path):
    data = pd.read_csv(path)
    elements = data['tag'].unique()
    transactions_ids = data['tweet_id'].unique()
    transactions = dict()

    for transaction_id in transactions_ids:
        transaction = set()
        transaction = transaction.union(data.loc[data['tweet_id'] == transaction_id]['tag'].unique())
        transactions[transaction_id] = transaction

    return DataSet(elements, transactions)
