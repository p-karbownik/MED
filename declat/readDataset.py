import pandas as pd
from bitarray import bitarray


class DataSet:

    def __init__(self, elements: list, transactions: dict, encode: dict, decode: dict):
        self.elements = elements
        self.transactions = transactions
        self.encode_dict = encode
        self.decode_dict = decode


def read_data_set(path):
    data = pd.read_csv(path)
    elements = data['tag'].unique()
    el_num = len(elements)

    elem_dict = dict()
    decode_dict = dict()
    for i in range(el_num):
        elem_dict[elements[i]] = i
        decode_dict[i] = elements[i]

    transactions_ids = data['tweet_id'].unique()
    transactions = dict()

    for transaction_id in transactions_ids:
        transaction_array = el_num * bitarray('0')
        elements_in_transaction = data.loc[data['tweet_id'] == transaction_id]['tag'].unique()
        for e in elements_in_transaction:
            transaction_array[elem_dict.get(e)] = True
        transactions[transaction_id] = transaction_array

    return DataSet(elements, transactions, elem_dict, decode_dict)
