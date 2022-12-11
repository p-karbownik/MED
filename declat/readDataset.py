import pandas as pd
import bitarray as ba


class DataSet:

    def __init__(self, elements, transactions):
        self.elements = elements
        self.transactions = transactions


def read_data_set(path):
    data = pd.read_csv(path)
    elements_list = data['tag'].unique()
    transactions = data['tweet_id'].unique()
    i = 0
    e_dict = {}

    for e in elements_list:
        e_dict[e] = i
        i = i + 1

    transactions_dict = {}

    for t in transactions:
        elements = data.loc[data['tweet_id'] == t]['tag'].unique()
        bitarray = ba.bitarray(len(e_dict))
        bitarray.setall(1)

        for e in elements:
            bitarray[e_dict[e]] = 0
        transactions_dict[t] = bitarray

    return DataSet(e_dict, transactions_dict)
